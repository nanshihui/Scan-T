#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
import scapytool
class ScapyTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.set_deal_num(1)
        self.add_work(['sniffer'])
    def task(self,req,threadname):
        print req
        print threadname+'执行被动扫描'+str(datetime.datetime.now())
        scapytool.initsniffer()
        print threadname+'执行被动扫描结束'+str(datetime.datetime.now())
        return ''