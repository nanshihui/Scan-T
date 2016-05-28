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


snifferdata().initindex()	



# create and save and article
# machinedata = default()
# machinedata.IP = """123.12.32.1"""
# machinedata.Port = 1
# machinedata.Timesearch = """2012-02-02 11:11:11:111"""
# machinedata.State = 'on'
# machinedata.Name='http'
# machinedata.Product= 'httpserver'
# machinedata.Version= '3.1'
# machinedata.Script= 'scrupt'
# machinedata.Detail= 'detail'
# machinedata.Id=123123
# machinedata.Head= 'head'
# machinedata.Hackinfo= 'hackinfo'
# machinedata.Keywords= 'keywords'
# machinedata.Disclosure= 'discolssd'
 
# machinedata.save()
# 

# data = default.getdata(id='12')
# data.delete()
# Display cluster health
# print(connections.get_connection().cluster.health())

#search

# ms = MultiSearch(index='test',doc_type='default')
# searcttext='scrupt'
# s=Search().query(Q("match", IP=searcttext) | 
# 											Q("match", Port=(int(searcttext) if searcttext.isdigit() else 0)) | 
# 											Q("match", Timesearch=searcttext) | 
# 											Q("match", State=searcttext) | 
# 											Q("match", Name=searcttext) | 
# 											Q("match", Product=searcttext) | 
# 											Q("match", Version=searcttext) | 
# 											Q("match", Script=searcttext) | 
# 											Q("match", Detail=searcttext) | 
# 											Q("match", Head=searcttext) | 
# 											Q("match", Hackinfo=searcttext) | 											
# 											Q("match", Keywords=searcttext) | 											
# 											Q("match", Disclosure=searcttext)  											
# )
# ms=ms.add(s)
# responses = ms.execute()



# for response in responses:
# 	print("Results for query %r." % response.search.query)
# 	try:
# 		for hit in response:

# 			print hit 
# 	except Exception,e:
# 		print e











# 
# c=Search().query('match',Timesearch='2012-03-00')
# c.execute()
# d=list(c)
# print len(d)
# for hit in d:
#     print hit