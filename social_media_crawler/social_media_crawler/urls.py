from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^posts/(?P<link>.*)$', views.fetch_posts_for_link),
    url(r'^admin/', include(admin.site.urls))
)
