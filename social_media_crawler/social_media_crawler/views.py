from __future__ import absolute_import
from rest_framework.decorators import *
from rest_framework.response import Response
from .celery import fetch_facebook_posts


@api_view(['GET'])
def fetch_posts_for_link(request, link):
    fetch_facebook_posts.delay(link)
    return Response()
