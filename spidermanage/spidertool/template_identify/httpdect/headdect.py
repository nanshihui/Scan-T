#!/usr/bin/python
#coding:utf-8
from spidertool.template_identify.httpdect.webdection import main
def dect(head='',context='',ip='',port=''):
#     webdection
    keywords=''
    hackinfo=''
    if port =='443':
        w = main.getwebinfo(ip,1)
    else:
        w = main.getwebinfo(ip,0)
    keywords= str(w)
    print keywords
    return keywords,hackinfo

# w = main.main('www.baidu.com',1)
# print w