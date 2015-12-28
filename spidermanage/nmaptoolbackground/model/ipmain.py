#!/usr/bin/python
#coding:utf-8
from spidertool import webtool
class Ip(object):
    def __init__(self,ip='',vendor='',osfamily='',osgen='',accurate='',state='',hostname='unknow',updatetime='',city=''):
        '''
        Constructor
        '''

        self.ip=ip
        self.vendor=vendor
        self.osgen=osgen
        self.osfamily=osfamily
        self.accurate=accurate
        if updatetime!='':
            self.updatetime=updatetime
        else:
            self.updatetime=webtool.getlocaltime()
   
        self.state=state
        self.hostname=hostname
        self.city=city
    def setIP(self,ip):
        self.ip=ip

    def setState(self,state):
        self.state=state

    def getIP(self):
        return self.ip
    def getVendor(self):
        return self.vendor
    def getOsfamily(self):
        return self.osfamily
    def getState(self):
        return self.state
    def getOsgen(self):
        return self.osgen
    def getUpdatetime(self):
        return self.updatetime
    def getAccurate(self):
        return self.accurate
    def getHostname(self):
        return self.hostname
    
    
    
    
    
    