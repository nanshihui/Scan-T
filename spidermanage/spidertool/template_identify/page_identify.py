#!/usr/bin/python
#coding:utf-8
from httpdect import headdect
from poc_file import pocsearchtask
def identify_main(head='',context='',ip='',port='',productname=''):
    keywords=''
    hackinfo=''
    keywords,hackinfo=headdect.dect(head=head,context=context,ip=ip,port=port)
    temp=pocsearchtask.getObject()
    temp.add_work([(head,context,ip,port,productname,keywords,hackinfo)])
    
#    dedeCMS()
#检测网站的产品    

    return keywords,hackinfo
