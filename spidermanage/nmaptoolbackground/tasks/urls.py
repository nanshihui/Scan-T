#!/usr/bin/python
#coding:utf-8
from django.conf.urls import url

import taskroute as route

urlpatterns = [
    url(r'^$', route.taskshow, name='taskshow'),
    url(r'^status/$', route.indexpage, name='status'),
    url(r'^taskquery/$', route.taskquery, name='taskquery'),
    url(r'^taskadd/$', route.taskadd, name='taskadd'),
    url(r'^taskstart/$', route.taskstart, name='taskstart'),
    url(r'^taskpause/$', route.taskpause, name='taskpause'),
    url(r'^taskdestroy/$', route.taskdestroy, name='taskdestroy'),

  
]