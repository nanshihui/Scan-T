# !/usr/bin/env python
# -*- coding:utf-8 -*-
from spidertool import zmaptool,iptask,sniffertask
import random
from datetime import datetime

import objgraph
operator = {'6':'3306','1':'80','2':'8080','3':'443','4':'22','5':'21','7':'873','8':'9200'}  
def tick():
    if sniffertask.getObject().get_length()>30:
        print('too much work: %s' % datetime.now())
        pass
    else:

        num=random.randint(1, 1)

        temp=zmaptool.getObject()

        temp.do_scan(port=operator.get(str(num)),num='20',needdetail='1')
    print('Tick! The time is: %s' % datetime.now())
def ticknormal():
    num=random.randint(1, 1)

    temp=zmaptool.getObject()
    
    temp.do_scan(port=operator.get(str(num)),num='30')
def gchelp():
    import gc
    gc.collect()
    print('Tick! The time is: %s' % datetime.now())
def listiptask():
    listitem=iptask.getObject()
    listitem.add_work([('172.20.13.11','172.20.13.12')])
    print '自定义任务已经启动'