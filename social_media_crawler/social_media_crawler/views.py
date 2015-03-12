from rest_framework.decorators import *
from rest_framework.response import Response
from django.conf import settings
import facebook

access_token = facebook.get_app_access_token(app_id=settings.FACEBOOK_APP_ID,
                                             app_secret=settings.FACEBOOK_SECRET_KEY)
graph = facebook.GraphAPI(access_token=access_token)


@api_view(['GET'])
def fetch_posts_for_link(request, link):
    id = get_graph_id_for_link(link)
    return Response(graph.get_connections(id=id, connection_name='posts'))


def get_graph_id_for_link(link):
    response = graph.request("", args={"ids": link})
    return response[link]['id']
