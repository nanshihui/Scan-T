from django.conf.urls import url

from . import nmaproute as views

urlpatterns = [
    url(r'^$', views.indexpage, name='index'),
]