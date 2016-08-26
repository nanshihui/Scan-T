#!/usr/bin/python
#coding:utf-8

from spidertool import webtool
from location import Location
class Port(object):
    def __init__(self,ip='',port='',timesearch='',state='',name='',product='',version='',script='',detail='',head='',city='',hackinfo='',disclosure='',keywords=None,webtitle='',webkeywords=''):
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
        self.disclosure=disclosure
        self.keywords=keywords
        self.webkeywords = webkeywords
        self.webtitle = webtitle

        if self.keywords is None:
            self.keywords=Location(ip=str(self.ip)).getData()
        else:
            try:

                data=eval(keywords)
                self.keywords=data
                if self.keywords.get('geoip',None) is None:
                    self.keywords = Location(ip=str(self.ip)).getData()
            except Exception,e:

                self.keywords = Location(ip=str(self.ip)).getData()
            # print self.keywords
            # print self.keywords['geoip']['country']
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
   
   
   
   