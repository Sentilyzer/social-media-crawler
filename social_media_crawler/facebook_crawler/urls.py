from django.conf.urls import patterns, url

import views

urlpatterns = patterns('facebook_crawler.views',
    url(r'^link/(?P<link>.*)$', views.fetch_posts_for_link)
)