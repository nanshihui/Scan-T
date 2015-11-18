#!/usr/bin/python
#coding:utf-8
import uuid
from spidertool import webtool
class Job(object):
    def __init__(self,jobname='',jobaddress='',priority='1',starttime='',username='',jobport='',jobstatus='1',jobid='',result='',endtime='',createtime='',argument=''):
        '''
        Constructor
        '''
#         jobstatus=1 //未启动
#         jobstatus=2 //排队中
#         jobstatus=3 //正在进行
#         jobstatus=4 //挂起
#         jobstatus=5 //已完成
#         jobstatus=6 //已终止
        self.jobname=jobname
        self.jobaddress=jobaddress
        self.priority=priority
        self.starttime=starttime
        self.username=username
        if createtime!='':
            self.createtime=createtime
        else:
            self.createtime=webtool.getlocaltime()
        if jobid!='':
            self.jobid=jobid
        else:
            self.jobid=uuid.uuid1()
        self.jobport=jobport
        self.jobstatus=jobstatus
        self.result=result
        self.endtime=endtime
        self.argument=argument
    def setPriority(self,priority):
        self.priority=priority
    def setArgument(self,argument):
        self.argument=argument
        
    def setResult(self,result):
        self.result=result
    def setJobstatus(self,jobstatus):
        self.jobstatus=jobstatus
    def getUsername(self):
        return self.username
    def getJobname(self):
        return self.jobname
    def getJobaddress(self):
        return self.jobaddress
    def getJobid(self):
        return self.jobid
    def getResult(self):
        return self.result
    def getPort(self):
        return self.jobport
    def getPriority(self):
        return self.priority 
    def getStatus(self):
        return self.jobstatus
    def getStarttime(self):
        return self.starttime
    def getCreatetime(self):
        return self.createtime
    def getArgument(self):
        return self.argument
    