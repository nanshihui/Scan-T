#!/usr/bin/python
#coding:utf-8
class SqlData(object):
    def __init__(self,func,dic):
        '''
        Constructor
        '''
        self.func=func
        self.dic=dic



    def getFunc(self):
        return self.func
    def getDic(self):
        return self.dic
