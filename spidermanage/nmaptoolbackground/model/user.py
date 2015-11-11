#!/usr/bin/python
#coding:utf-8
class User(object):
    def __init__(self,username='',password='',role='',power=1):
        '''
        Constructor
        '''
        self.jobname=jobname
        self.jobaddress=jobaddress
        self.jobport=jobport
        self.priority=priority
        self.arguments=arguments
        self.result=result
        self.status=status
    def setPriority(self,priority):
        self.priority=priority
    def setAddress(self,address):
        self.jobaddress=address
    def setStatus(self,status):
        self.status=status
    def setResult(self,result):
        self.result=result
    def getResult(self):
        return self.result
    def getAddress(self):
        return self.jobaddress
    def getPort(self):
        return self.jobport
    def getArguments(self):
        return self.arguments
    