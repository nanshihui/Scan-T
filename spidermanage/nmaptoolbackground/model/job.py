#!/usr/bin/python
#coding:utf-8
import uuid
class Job(object):
    def __init__(self,jobname='',jobaddress='',priority='1',starttime='',username='',jobport='',jobstatus='1'):
        '''
        Constructor
        '''
        self.jobname=jobname
        self.jobaddress=jobaddress
        self.priority=priority
        self.starttime=starttime
        self.username=username
        self.jobid=uuid.uuid1()
        self.jobport=jobport
        self.jobstatus=jobstatus
        self.result=''
    def setPriority(self,priority):
        self.priority=priority
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
    
    
    
    