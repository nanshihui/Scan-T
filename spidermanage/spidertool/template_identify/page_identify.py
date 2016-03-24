#!/usr/bin/python
#coding:utf-8
from httpdect import headdect
from poc_file import pocsearchtask
import gc,objgraph
def identify_main(head='',context='',ip='',port='',productname='',protocol='',nmapscript=''):
    keywords=''
    hackinfo=''
#     print '运行前状态'
#     gc.collect()
#     objgraph.show_growth()
    
    keywords,hackinfo=headdect.dect(head=head,context=context,ip=ip,port=port,protocol=protocol)
    temp=pocsearchtask.getObject()
    temp.add_work([(head,context,ip,port,productname,keywords,nmapscript,protocol)])
     
#     gc.collect()
#     objgraph.show_growth()
#     print '检测运行后状态'
    return keywords,hackinfo
