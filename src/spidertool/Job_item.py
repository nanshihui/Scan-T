# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2015年11月4日

@author: dell
'''

class Job_Item(object):
    '''
    classdocs
    '''


    def __init__(self,jobname='',jobaddress=[],jobport=[],priority=1,result=[],status=0,arguments=''):
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
    
        
        