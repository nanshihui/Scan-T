#!/usr/bin/python
#coding:utf-8
from django.conf.urls import url

from . import searchroute as route

urlpatterns = [
    url(r'^$', route.indexpage, name='search'),
    url(r'^searchdetail/$', route.detailpage, name='searchdetail'),

    
    
]