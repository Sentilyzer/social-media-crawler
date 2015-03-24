from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks import fetch_facebook_posts


@api_view(['GET'])
def fetch_posts_for_link(request, link):
    fetch_facebook_posts.delay(link)
    return Response()
