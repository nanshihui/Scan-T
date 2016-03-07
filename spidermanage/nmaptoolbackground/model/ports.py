#!/usr/bin/python
#coding:utf-8

from spidertool import webtool
class Port(object):
    def __init__(self,ip='',port='',timesearch='',state='',name='',product='',version='',script='',detail='',head='',city='',hackinfo=''):
        '''
        Constructor
        '''
        self.ip=ip
        self.port=port
        self.version=version
        self.state=state
        self.name=name
        if timesearch!='':
            self.timesearch=timesearch
        else:
            self.timesearch=webtool.getlocaltime()

        self.product=product
        self.script=script
        self.detail=detail
        self.head=head
        self.city=city
        self.hackinfo=hackinfo
    def getIP(self):
        return self.ip
    def getPort(self):
        return self.port
    def getVersion(self):
        return self.version
    def getState(self):
        return self.state
    def getName(self):
        return self.name
    def getTime(self):
        return self.timesearch
    def getProduct(self):
        return self.product 
    def getScript(self):
        return self.script
    def getHead(self):
        return self.head
   
   
   
   