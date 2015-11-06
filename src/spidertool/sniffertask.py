#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
class snifferTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.connectpool=connectpool.ConnectPool()
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())
        
        ans = self.connectpool.getConnect(req)
        
        print threadname+'任务结束'+str(datetime.datetime.now())
        return ans





