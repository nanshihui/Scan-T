#!/usr/bin/python
#coding:utf-8


from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer,MultiSearch,Search,Q
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class snifferdata(DocType):
    IP = String(analyzer='ik')
    Port = Integer()
    Timesearch = String(analyzer='ik')
    State = String(analyzer='ik')
    Name= String(index='not_analyzed')
    Product= String(analyzer='ik')
    Version= String(analyzer='ik')
    Script= String(analyzer='ik')
    Detail= String(analyzer='ik')
    Id=Integer()
    Head= String(analyzer='ik')
    Hackinfo= String(analyzer='ik')
    Keywords= String(analyzer='ik')
    Disclosure= String(analyzer='ik') 
    class Meta:
        index = 'datap'

    def save(self, ** kwargs):
        return super(default, self).save(** kwargs)
    def initindex(self):
        self.init()
    @classmethod
    def getdata(cls,**kwargs):
        try:
            data=cls.get(**kwargs)
            print data
            return data
        except Exception, e:
            print e

class ip_maindata(DocType):
    IP = String(analyzer='ik')
    Vendor = String(analyzer='ik')
    Osfamily = String(analyzer='ik')
    Osgen = String(analyzer='ik')
    Accurate= String(index='not_analyzed')
    Updatetime= String(analyzer='ik')
    Hostname= String(analyzer='ik')
    State= String(analyzer='ik')
    Mac= String(index='not_analyzed')
    Country=Integer()
    Country_id= String(index='not_analyzed')
    Area= String(index='not_analyzed')
    Area_id= Integer() 
    Region= String(index='not_analyzed') 
    Region_id= String(index='not_analyzed') 
    City= String(index='not_analyzed') 
    City_id= Integer() 
    County= String(index='not_analyzed') 
    County_id= Integer() 
    Isp= String(index='not_analyzed') 
    Isp_id= Integer() 

    class Meta:
        index = 'datap'

    def save(self, ** kwargs):
        return super(default, self).save(** kwargs)
    def initindex(self):
        self.init()
    @classmethod
    def getdata(cls,**kwargs):
        try:
            data=cls.get(**kwargs)
            print data
            return data
        except Exception, e:
            print e
# snifferdata().initindex()   
ip_maindata().initindex()   




 