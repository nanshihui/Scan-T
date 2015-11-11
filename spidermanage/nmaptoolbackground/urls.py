from django.conf.urls import url

from . import nmaproute as route

urlpatterns = [
    url(r'^$', route.login, name='login'),
    url(r'^login/$', route.login, name='login'),
    url(r'^mainpage/$', route.indexpage, name='index'),
]