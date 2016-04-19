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
from elasticsearch_dsl import DocType, String, Date, Integer
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

	def init(self):
		self.init()
		
		
# create the mappings in elasticsearch


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
article = Snifferdata_ela.get(Script='scrupt',Id=123123)
print(article)

# Display cluster health
# print(connections.get_connection().cluster.health())