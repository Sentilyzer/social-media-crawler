from __future__ import absolute_import
from django.utils.dateparse import parse_datetime
import facebook
import os

from celery import Celery, chain
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_crawler.settings')

app = Celery('social_media_crawler')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from .models import Post

access_token = facebook.get_app_access_token(app_id=settings.FACEBOOK_APP_ID,
                                             app_secret=settings.FACEBOOK_SECRET_KEY)
graph = facebook.GraphAPI(access_token=access_token)


@app.task(bind=True)
def fetch_facebook_posts(self, link):
    chain(get_posts_for.s(link), save_posts.s())()


@app.task(bind=True)
def get_posts_for(self, graph_id):
    return graph.request(graph_id + "/posts", args={"fields":
                                                        "id,from,type,status_type,message,story,created_time,updated_time,shares,likes.limit(1).summary(true),comments.limit(1).summary(true)"})


@app.task(bind=True)
def save_posts(self, data):
    for post_data in data['data']:
        create_post(post_data)


def create_post(post_data):
    post = Post()
    post.name = post_data['from']['name']
    post.text = post_data['message']
    post.date = parse_datetime(post_data['created_time'])
    if 'shares' in post_data:
        post.shares = int(post_data['shares']['count'])
    if 'likes' in post_data:
        post.likes = int(post_data['likes']['summary']['total_count'])
    post.save()

    for comment_data in post_data['comments']:
        create_comment(comment_data, post)


def create_comment(comment_data, parent_post):
    comment = Post()
    comment.name = comment_data['from']['name']
    comment.text = comment_data['message']
    comment.date = parse_datetime(comment_data['created_time'])
    if 'shares' in comment_data:
        comment.shares = int(comment_data['shares']['count'])
    if 'likes' in comment_data:
        comment.likes = int(comment_data['likes']['summary']['total_count'])
    comment.replyto = parent_post

    comment.save()
