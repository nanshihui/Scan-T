#!/usr/bin/python
#coding:utf-8
import sys;
reload(sys);

sys.setdefaultencoding('utf8');
from elasticsearch_dsl.query import MultiMatch, Match
from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer,MultiSearch,Search,Q
from elasticsearch_dsl.connections import connections
import mapping
from logger import initLog
import chardet
logger = initLog('logs/elastic.log', 2, True)
# Define a default Elasticsearch client
# connections.create_connection(hosts=['localhost'])
import base64
def decodestr(msg):

    chardit1 = chardet.detect(msg)

    try:
        # print chardit1['encoding'],msg.decode('gbk')
        if chardit1['encoding']=='utf-8' :
            return msg
        else:
            if  chardit1['encoding']=='ISO-8859-2':
                return msg.decode('gbk')
            else:
                if 'charset=gbk' in msg:

                    return msg.decode('gbk')
                else:
                    return msg.decode(chardit1['encoding']).encode('utf-8')

    except Exception,e:
        return str(msg)
def getproperty(dic,property):
    return decodestring(str(dic.get(property,' ')))
def decodestring(msg):

    if str:
        try:

            return decodestr(msg.decode('string_escape').decode('string_escape'))
        except Exception,e:
            print e,42




    else:
        return ' '


def get_table_obj(_cls_name):  
    obj =  getattr(mapping,_cls_name)  
    return obj 
def setvalue(instance,key,value):
	setattr(instance, key, value)
# data = mapping.snifferdata.getdata(id='116.13.94.6:80')
# data.delete()

def default():
    print 'there is error'
def inserttableinfo_byparams(table,select_params,insert_values,extra='',updatevalue=None,primarykey=1):

    instanceins=None
    if table=='snifferdata':
        primarykey=2

    instanceins=None

        
    
    instanceitem=None

    for item in insert_values:
        eachitem=None
        if type(item).__name__=='str':
            eachitem=tuple(item)
        else:
            eachitem=item
        instanceins= get_table_obj(table)
        # logger and logger.info('get each insert: %s', eachitem)
        if extra or updatevalue:
            # logger and logger.info('更新数据')
            instanceitem = instanceins.getdata(id=':'.join(eachitem[:primarykey]))
            logger and logger.info(str(instanceitem))
            if instanceitem is None:
                # logger and logger.info('找不到该数据，创建数据')
                instanceins=get_table_obj(table)
                instanceitem=instanceins(meta={'id': ':'.join(eachitem[:primarykey])})
        else:
            instanceitem=instanceins(meta={'id': ':'.join(eachitem[:primarykey])})

        for i in xrange(0,len(select_params)):


            # logger and logger.info('更新数据%s :%s',select_params[i],decodestr(str(eachitem[i])))
            setvalue(instanceitem,select_params[i],decodestr(str(eachitem[i])))
        try:
            res=instanceitem.save()
        except Exception,e:
            logger and logger.error('error: %s', str(e))
        else:
            logger and logger.info('insert success')
def replaceinserttableinfo_byparams(table,select_params,insert_values,primarykey=1):
    inserttableinfo_byparams(table,select_params,insert_values,primarykey=primarykey)
# inserttableinfo_byparams('snifferdata', ['ip','port','product'], [('1','2','http')],primarykey=2)

def search(page='0',dic=None,content=None):

    limitpage=15
    validresult=False
    if content is not None:
        q=Q("multi_match", query=content, fields=['ip', 'name','product',
                'script' ,'detail' ,'head'  ,'hackinfo','keywords' ,'disclosure'  ])
          
    else:
        searcharray=[]
        keys=dic.keys()
        for key in keys:
            if key=='name':
                searcharray.append(Q('term', name=dic[key]))
            if key=='ip':
                searcharray.append(Q('term', ip=dic[key]))
            if key=='port':
                searcharray.append(Q('term', port=dic[key]))
            if key=='state':
                searcharray.append(Q('term', state=dic[key]))
            if key=='timesearch':
                searcharray.append(Q('match', timesearch=dic[key]))                 
            if key=='keywords':
                searcharray.append(Q('match', keywords=dic[key]))                     
            if key=='product':
                searcharray.append(Q('match', product=dic[key]))                       
            if key=='version':
                searcharray.append(Q('match', version=dic[key]))                   
            if key=='script':
                searcharray.append(Q('match', script=dic[key]))               
            if key=='hackinfo':
                searcharray.append(Q('match', hackinfo=dic[key]))
            if key=='head':
                searcharray.append(Q('match', head=dic[key]))                
            if key=='detail':
                searcharray.append(Q('match', detail=dic[key]))                
            if key=='disclosure':
                searcharray.append(Q('match', disclosure=dic[key]))              
                
        q=Q('bool', must=searcharray)
    s = Search(index='datap',doc_type='snifferdata').query(q)



#     s = Search.from_dict({"query": {
#     "bool":{
#             "must":[               
#                 {
#                     "term":{"name":"http"},
#                     "term":{"port":"80"},
#                      
#                 },
#                 {
#                     "match":{"head":"manager"},
#                      "match":{"head":"200"},
#                 }
#                 ]
#         }
# 
# }
# })
    s= s[int(page)*limitpage:int(page)*limitpage+limitpage]

    response = s.execute()
    if response.success():
        



        portarray=[]
        count= response.hits.total
        print '返回的集中率为%d' % count
        if count == 0:
            pagecount = 0;
        elif count %limitpage> 0:

            pagecount=int((count+limitpage-1)/limitpage) 


        else:
            pagecount = count / limitpage
        from nmaptoolbackground.model import ports
        count=len(response)
        print '返回的实际数量为%d' % count 
        if count>0:
            for temp in response :
                dic=temp.to_dict()
                aport=ports.Port(ip=getproperty(dic,'ip'),port=getproperty(dic,'port'),timesearch=getproperty(dic,'timesearch'),state=getproperty(dic,'state'),name=getproperty(dic,'name'),product=getproperty(dic,'product'),version=getproperty(dic,'version'),script=base64.b64encode(getproperty(dic,'script')),detail=getproperty(dic,'detail'),head=getproperty(dic,'head'),city='',hackinfo=getproperty(dic,'hackinfo'),disclosure=getproperty(dic,'disclosure'))

                # ip=getproperty(dic,'ip')
                # port=getproperty(dic,'port')
                # timesearch=getproperty(dic,'timesearch')
                # state=getproperty(dic,'state')
                # name=getproperty(dic,'name')
                # product=getproperty(dic,'product')
                # version=getproperty(dic,'version')
                # script=base64.b64encode(getproperty(dic,'script'))
                # detail=getproperty(dic,'detail')
                # head=getproperty(dic,'head')
                # city=''
                # hackinfo=getproperty(dic,'hackinfo')
                # disclosure=getproperty(dic,'disclosure')


                portarray.append(aport)

        return portarray,count,pagecount



    else:
        print '查询失败'
        return [],0,0


# print ":".join(map(str, item[:3]))
# data = default.getdata(id='12')
# data.delete()
# Display cluster health
# print(connections.get_connection().cluster.health())

#search

# ms = MultiSearch(index='datap',doc_type='snifferdata')
# searcttext='http'
# s=Search().query(Q("match", IP=searcttext) | 
# # 											Q("match", Port=(int(searcttext) if searcttext.isdigit() else 0)) | 
# # 											Q("match", Timesearch=searcttext) | 
# # 											Q("match", State=searcttext) | 
# 											Q("match", Name=searcttext) | 
# 											Q("match", Product=searcttext) | 
# # 											Q("match", Version=searcttext) | 
# 											Q("match", Script=searcttext) | 
# 											Q("match", Detail=searcttext) | 
# 											Q("match", Head=searcttext) | 
# 											Q("match", Hackinfo=searcttext) | 											
# 											Q("match", Keywords=searcttext) | 											
# 											Q("match", Disclosure=searcttext)  											
# )
# ms=ms.add(s)
# responses = ms.execute()
# 
# 
# 
# 
# 
# for response in responses:
#     print("Results for query %r." % response.search.query)
#     try:
#         for hit in response:
#             print hit.doc_types
#     except Exception,e:
#         print e







# 
# c=Search().query('match',Timesearch='2012-03-00')
# c.execute()
# d=list(c)
# print len(d)
# for hit in d:
#     print hit
#     
    
    
if __name__ == '__main__':
    # print search(page='0', dic=None, content='218.28.144.77')
    print '\xD6\xD0\xB9\xFA\xD1\xCC\xB2\xDD\xC5\xE0\xD1\xB5\xCD\xF8'.decode('gbk')