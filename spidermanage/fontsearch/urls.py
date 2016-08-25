#!/usr/bin/python
#coding:utf-8
from django.conf.urls import url

from . import searchroute as route

urlpatterns = [
    url(r'^$', route.indexpage, name='search'),
    url(r'^searchmain/$', route.mainpage, name='searchmain'),
    url(r'^searchdetail/$', route.detailpage, name='searchdetail'),
    url(r'^mapsearch/$', route.mapsearch, name='mapsearch'),
    url(r'^mapsearchmain/$', route.mapsearchmain, name='mapsearchmain'),
    url(r'^detailmapview/$', route.detailmapview, name='detailmapview'),
    url(r'^map/$', route.map, name='map'),
    url(r'^ipinfo/$', route.ipinfo, name='ipinfo'),

    
    
]