# !/usr/bin/env python
# -*- coding:utf-8 -*-
from spidertool import zmaptool,iptask
import random
from datetime import datetime
operator = {'6':'3306','1':'80','2':'8080','3':'443','4':'22','5':'21','7':'873','8':'9200'}  
def tick():
    num=random.randint(8, 8)

    temp=zmaptool.Zmaptool()
    
    temp.do_scan(port=operator.get(str(num)),num='12',needdetail='1')
    print('Tick! The time is: %s' % datetime.now())
def ticknormal():
    num=random.randint(8, 8)

    temp=zmaptool.Zmaptool()
    
    temp.do_scan(port=operator.get(str(num)),num='30')
    print('Tick! The time is: %s' % datetime.now())
def listiptask():
    listitem=iptask.getObject()
    listitem.add_work([('172.20.13.11','172.20.13.12')])
    print '自定义任务已经启动'