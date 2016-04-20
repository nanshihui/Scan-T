#!/usr/bin/python
#coding:utf-8

# from datetime import datetime
# from elasticsearch import Elasticsearch
# es=Elasticsearch([{'host': 'localhost', 'port': 9200}])
# es.indices.create(index='asd',ignore=400)
# res=es.index(index='asd',doc_type='snifferdata',body={
# 		"any":"data", 
# 		"timestamp": datetime.now(),
# 		'other':12

# 	})
# print res
# print(res['created'])
# try:
# 	res = es.get(index="asd", doc_type='snifferdata')
# 	print(res['_source'])
# except:
# 	print 'can not get'
# try:
# 	res = es.search(index="asd", body={"query": {"match_all": {}}})
# 	print("Got %d Hits:" % res['hits']['total'])
# 	for hit in res['hits']['hits']:
# 		print("%(any)s %(timestamp)s" % hit["_source"])
# except:
# 	print 'can not search'
##

"""
select ip as IP,
port as Port,
timesearch as Timesearch,
state as State,
name as Name,
product as Product,
version as Version,
script as Script,
detail as Detail,
id as Id,
head as Head,
hackinfo as Hackinfo,
keywords as Keywords,
disclosure as Disclosure from snifferdata"""

###
from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer,MultiSearch,Search,Q
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class Snifferdata_ela(DocType):
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
		index = 'snifferdata'

	def save(self, ** kwargs):
		return super(Snifferdata_ela, self).save(** kwargs)

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
 			
		



# create and save and article
# machinedata = Snifferdata_ela()
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
#  
# machinedata.save()
# 

# data = Snifferdata_ela.getdata(id='42')

# Display cluster health
# print(connections.get_connection().cluster.health())

#search

ms = MultiSearch(index='snifferdata')
searcttext='http'
s=Search().query(Q("match", IP=searcttext) | 
											Q("match", Port=(int(searcttext) if searcttext.isdigit() else 0)) | 
											Q("match", Timesearch=searcttext) | 
											Q("match", State=searcttext) | 
											Q("match", Name=searcttext) | 
											Q("match", Product=searcttext) | 
											Q("match", Version=searcttext) | 
											Q("match", Script=searcttext) | 
											Q("match", Detail=searcttext) | 
											Q("match", Head=searcttext) | 
											Q("match", Hackinfo=searcttext) | 											
											Q("match", Keywords=searcttext) | 											
											Q("match", Disclosure=searcttext)  											
)
ms=ms.add(s)
responses = ms.execute()

# 
# c=Search().query('match',Timesearch='2012-03-00')
# c.execute()
# d=list(c)
# print len(d)
# for hit in d:
#     print hit

for response in responses:
	print("Results for query %r." % response.search.query)
	try:
		for hit in response:

			print hit 
	except Exception,e:
		print e
