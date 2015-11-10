from django.conf.urls import url

from . import nmaproute as route

urlpatterns = [
    url(r'^$', route.indexpage, name='index'),
]