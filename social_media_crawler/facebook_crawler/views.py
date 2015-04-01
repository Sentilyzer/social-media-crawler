from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks import fetch_facebook_posts


@api_view(['GET'])
def fetch_posts_for_link(request, link):

    answer_url = request.GET.get('answer', None)

    fetch_facebook_posts.delay(link, answer_url)

    return Response()
