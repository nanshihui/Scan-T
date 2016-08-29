# !/usr/bin/env python
# -*- coding:utf-8 -*-
from spidertool import zmaptool,iptask,sniffertask,SQLTool
import random
from datetime import datetime
operator = {'6':'3306','1':'80','2':'8080','3':'443','4':'22','5':'21','7':'873','8':'2375'}
def text():
    print('Tick! The time is: %s' % datetime.now())
def tick():
    if sniffertask.getObject().get_length() > 30:
        print('too much work: %s' % datetime.now())
        pass
    else:

        num = random.randint(1, 1)

        temp = zmaptool.getObject()

        temp.do_scan(port=operator.get(str(num)), num='20', needdetail='1')
    print('Tick! The time is: %s' % datetime.now())
def zmaptask():
    num=random.randint(8, 8)

    temp=zmaptool.Zmaptool()

    temp.do_scan(port=operator.get(str(num)),num='20')
    print('Tick! The time is: %s' % datetime.now())
def listiptask():
    listitem=iptask.getObject()
    listitem.add_work([('172.20.13.11','172.20.13.12')])
    print '自定义任务已经启动'
