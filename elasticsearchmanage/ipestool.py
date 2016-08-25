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

import base64
def ipsearch(page='0',dic=None,content=None):

    limitpage=15
    validresult=False
    orderlabel=0
    orderarray = []
    if content is not None:
        q=Q("multi_match", query=content, fields=['ip', 'city','vendor',
                'isp' ,'region' ,'country'  ,'updatetime','county' ,'osfamily'  ])

    else:
        searcharray=[]
        keys=dic.keys()
        orderlabel=0

        for key in keys:
            if key=='city':
                searcharray.append(Q('term', city=dic[key]))
            if key=='ip':
                searcharray.append(Q('term', ip=dic[key]))
            if key=='isp':
                searcharray.append(Q('term', isp=dic[key]))
            if key=='region':
                searcharray.append(Q('term', region=dic[key]))

            if key=='order':
                orderarray.append(dic[key])
                orderlabel=1


        q=Q('bool', must=searcharray)

    if orderlabel==0:
        s = Search(index='datap', doc_type='ip_maindata').query(q)
    else:
        s=Search(index='datap', doc_type='ip_maindata').query(q).sort(orderarray[0])






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
        from nmaptoolbackground.model import ipmain
        count=len(response)
        print '返回的实际数量为%d' % count
        from elastictool import getproperty
        if count>0:
            for temp in response :
                dic=temp.to_dict()
                aip=ipmain.Ip(ip=getproperty(dic,'ip'),vendor=getproperty(dic,'vendor'),osfamily=getproperty(dic,'osfamily'),osgen=getproperty(dic,'osgen'),accurate=getproperty(dic,'accurate'),state=getproperty(dic,'state'),hostname=getproperty(dic,'hostname'),updatetime=getproperty(dic,'updatetime'),city=getproperty(dic,'city'),isp=getproperty(dic,'isp'),county=getproperty(dic,'county'),country=getproperty(dic,'country'),region=getproperty(dic,'region'))




                portarray.append(aip)

        return portarray,count,pagecount



    else:
        print '查询失败'
        return [],0,0
