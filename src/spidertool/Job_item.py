'''
Created on 2015年11月4日

@author: dell
'''
# !/usr/bin/env python
# -*- coding:utf-8 -*-
class Job_Item(object):
    '''
    classdocs
    '''


    def __init__(self,jobname='',jobaddress='',jobport=[],priority=1,result=[]):
        '''
        Constructor
        '''
        self.jobname=jobname
        self.jobaddress=jobaddress
        self.jobport=jobport
        self.priority=priority
        self.result=result
        