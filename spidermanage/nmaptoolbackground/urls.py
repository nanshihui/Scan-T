from django.conf.urls import url

from . import nmaproute as route

urlpatterns = [
    url(r'^$', route.indexpage, name='login'),
    url(r'^login/$', route.login, name='login'),
    url(r'^logout/$', route.logout, name='logout'),
    url(r'^mainpage/$', route.indexpage, name='index'),
    url(r'^taskdetail/$',route.taskdetail,name='taskdetail'),
    url(r'^taskdetail/eachtask/$',route.ipmain,name='ipmain'),
    url(r'^jobshow/$',route.jobshow,name='jobshow'),
    url(r'^jobadd/$',route.jobadd,name='jobadd')
    
]