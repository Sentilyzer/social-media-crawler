from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook/', include('facebook_crawler.urls'))
)
