#!/usr/bin/python
#coding:utf-8
from webdection import main

def dect(head='',context='',ip='',port='',protocol=''):
#     webdection
    keywords=''
    hackinfo=''
    if port =='443':
        w = main.getwebinfo(ip+':'+port,1)
    else:
        ip=protocol+'://'+ip
        w = main.getwebinfo(ip+':'+port,0)
    keywords= str(w)
    print keywords
    return keywords,hackinfo

# w = main.getwebinfo('www.baidu.com',1)
# print w