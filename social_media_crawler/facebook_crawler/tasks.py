from __future__ import absolute_import
from django.utils.dateparse import parse_datetime

from celery import shared_task, chain
from .models import Post
from .facebook import graph


@shared_task(bind=True)
def fetch_facebook_posts(self, link):
    chain(get_posts_for.s(link), save_posts.s())()


@shared_task(bind=True)
def get_posts_for(self, graph_id):
    return graph.request(graph_id + "/posts", args={"fields":
                                                        "id,from,type,status_type,message,story,created_time,updated_time,shares,likes.limit(1).summary(true),comments.limit(1).summary(true)"})

@shared_task(bind=True)
def save_posts(self, data):
    for post_data in data['data']:
        create_post(post_data)


def create_post(post_data):
    post = Post()
    post.graph_id = post_data['id']
    post.name = post_data['from']['name']
    post.text = post_data['message']
    post.date = parse_datetime(post_data['created_time'])
    if 'shares' in post_data:
        post.shares = int(post_data['shares']['count'])
    if 'likes' in post_data:
        post.likes = int(post_data['likes']['summary']['total_count'])
    post.save()

    if 'comments' in post_data:
        for comment_data in post_data['comments']['data']:
            create_comment(comment_data, post)


def create_comment(comment_data, parent_post):
    comment = Post()
    comment.graph_id = comment_data['id']
    comment.name = comment_data['from']['name']
    comment.text = comment_data['message']
    comment.date = parse_datetime(comment_data['created_time'])
    if 'shares' in comment_data:
        comment.shares = int(comment_data['shares']['count'])
    if 'likes' in comment_data:
        comment.likes = int(comment_data['likes']['summary']['total_count'])
    comment.replyto = parent_post

    comment.save()
