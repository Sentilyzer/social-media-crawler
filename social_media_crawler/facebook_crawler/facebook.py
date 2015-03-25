from __future__ import absolute_import

from .settings import FACEBOOK_SECRET_KEY, FACEBOOK_APP_ID
import facebook

_access_token = facebook.get_app_access_token(app_id=FACEBOOK_APP_ID,
                                              app_secret=FACEBOOK_SECRET_KEY)
graph = facebook.GraphAPI(access_token=_access_token)
