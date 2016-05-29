#!/usr/bin/python
#coding:utf-8


from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer,MultiSearch,Search,Q
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class snifferdata(DocType):
    ip = String(analyzer='ik')
    port = String()
    timesearch = String(analyzer='ik')
    state = String(analyzer='ik')
    name= String(index='not_analyzed')
    product= String(analyzer='ik')
    version= String(analyzer='ik')
    script= String(analyzer='ik')
    detail= String(analyzer='ik')
    id=String()
    head= String(analyzer='ik')
    hackinfo= String(analyzer='ik')
    keywords= String(analyzer='ik')
    disclosure= String(analyzer='ik') 
    class Meta:
        index = 'datap'

    def save(self, ** kwargs):
        return super(snifferdata, self).save(** kwargs)
    def initindex(self):
        self.init()
    def saysomething(self):
        print 'say something'
    @classmethod
    def getdata(cls,**kwargs):
        try:
            data=cls.get(**kwargs)
            print data
            return data
        except Exception, e:
            print e

class ip_maindata(DocType):
    ip = String(analyzer='ik')
    vendor = String(analyzer='ik')
    osfamily = String(analyzer='ik')
    osgen = String(analyzer='ik')
    accurate= String(index='not_analyzed')
    updatetime= String(analyzer='ik')
    hostname= String(analyzer='ik')
    state= String(analyzer='ik')
    mac= String(index='not_analyzed')
    country=String()
    country_id= String(index='not_analyzed')
    area= String(index='not_analyzed')
    area_id= String() 
    region= String(index='not_analyzed') 
    region_id= String(index='not_analyzed') 
    city= String(index='not_analyzed') 
    city_id= String() 
    county= String(index='not_analyzed') 
    county_id= String() 
    isp= String(index='not_analyzed') 
    isp_id= String() 

    class Meta:
        index = 'datap'

    def save(self, ** kwargs):
        return super(ip_maindata, self).save(** kwargs)
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
if __name__ == "__main__":
    snifferdata().initindex()   
    ip_maindata().initindex() 
    print '创建索引成功'  




 