#!/usr/bin/python
#coding:utf-8


from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer,MultiSearch,Search,Q
from elasticsearch_dsl.connections import connections
import mapping
from logger import initLog
logger = initLog('logs/elastic.log', 2, True)
# Define a default Elasticsearch client
# connections.create_connection(hosts=['localhost'])
def get_table_obj(_cls_name):  
    obj =  getattr(mapping,_cls_name)  
    return obj 
def setvalue(instance,key,value):
	setattr(instance, key, value)
# data = mapping.snifferdata.getdata(id='12')
# data.delete()

def default():
    print 'there is error'
def inserttableinfo_byparams(table,select_params,insert_values,extra=' ',updatevalue=None,primarykey=1):
    print table,select_params,insert_values
    instanceins=None
    if table=='snifferdata':
        primarykey=2
    instanceins=get_table_obj(table)
    instanceitem=None

    for item in insert_values:
        eachitem=None
        if type(item).__name__=='str':
            eachitem=tuple(item)
        else:
            eachitem=item

        logger and logger.info('get each insert: %s', eachitem)
        instanceitem=instanceins(meta={'id': ':'.join(eachitem[:primarykey])})

        logger and logger.info('get primarykey: %s', instanceitem)
        for i in xrange(0,len(select_params)):

            logger and logger.info('set the value: %s : %s', select_params[i],eachitem[i])

            setvalue(instanceitem,select_params[i],eachitem[i])
        try:
            res=instanceitem.save()
        except Exception,e:
            logger and logger.error('error: %s', str(e))
        else:
            logger and logger.info('insert success')
def replaceinserttableinfo_byparams(table,select_params,insert_values,primarykey=1):
    inserttableinfo_byparams(table,select_params,insert_values,primarykey=primarykey)
# inserttableinfo_byparams('snifferdata', ['IP','Port','Name'], ['1','2','http'],primarykey=2)

# item=('1','2','3')
# print ':'.join( item[:3] )
# print map(str, item[:3])
# print ":".join(map(str, item[:3]))
# data = default.getdata(id='12')
# data.delete()
# Display cluster health
# print(connections.get_connection().cluster.health())

#search

# ms = MultiSearch(index='datap',doc_type='snifferdata')
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
#     
    
    
    