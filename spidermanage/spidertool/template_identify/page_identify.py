#!/usr/bin/python
#coding:utf-8
from httpdect import headdect
def identify_main(head='',context='',ip='',port=''):
    keywords=''
    hackinfo=''
    keyword,hackinfo=headdect.dect(head=head,context=context)
#    dedeCMS()
#检测网站的产品    

    return keywords,hackinfo
