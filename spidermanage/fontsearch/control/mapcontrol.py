#!/usr/bin/python
#coding:utf-8
from spidertool import SQLTool ,config


limitpage=15
DBhelp=None

def mapshow(ip='',port='',state='',name='',product='',version='',searchcontent='',isdic=1):
    localconfig=config.Config()
    table=localconfig.porttable
    iptable=localconfig.iptable
    validresult=False
    request_params=[]
    values_params=[]

    if ip!='':
        request_params.append(table+'.'+'ip')
        values_params.append(SQLTool.formatstring(ip))
    if port!='':
        request_params.append('port')
        values_params.append(SQLTool.formatstring(port))

    if state!='':
        request_params.append(table+'.'+'state')
        values_params.append(SQLTool.formatstring(state))
    if name!='':
        request_params.append('name')
        values_params.append(SQLTool.formatstring(name))
    if product!='':
        request_params.append('product')
        values_params.append(SQLTool.formatstring(product))
    if version!='':
        request_params.append('version')
        values_params.append(SQLTool.formatstring(version))

    global DBhelp

    DBhelp=SQLTool.DBmanager()
    DBhelp.connectdb()
    size = 0
    content=None
    result=None
    sql=""""""
    if isdic==0:
        if searchcontent =='':
            sql="""SELECT city, COUNT(*) FROM ip_maindata  GROUP BY city"""
        else:
            sql="""SELECT city, COUNT(*) FROM (SELECT ip AS ipitem FROM snifferdata WHERE MATCH (version , product , head , detail , script , hackinfo , disclosure , keywords) AGAINST ('%s' IN BOOLEAN MODE)
    GROUP BY ip) AS iptable LEFT JOIN ip_maindata ON ipitem = ip_maindata.ip GROUP BY city""" %(searchcontent)
    else:
        sql="""SELECT city, COUNT(*) FROM (SELECT ip AS ipitem FROM snifferdata WHERE  """
        request_params_length=len(request_params)
        for k in range(0, request_params_length - 1):
            sql = sql + request_params[k] + ' = ' + values_params[k] +' and '
        sql = sql + request_params[request_params_length - 1] + ' = ' + values_params[request_params_length - 1] + '  '

        sql = sql + """ GROUP BY ip) AS iptable LEFT JOIN ip_maindata ON ipitem = ip_maindata.ip GROUP BY city """
    try:
         result,content,count,col=DBhelp.searchtableinfo_byparams(table=sql,usesql=1)
    except Exception,e:
         print str(e)+'portcontrol 69'
         if DBhelp is not None:
             DBhelp.closedb()
         return [],0,0
    if DBhelp is not None:
         DBhelp.closedb()
         DBhelp=None
            

    portarray=[]
    if count>0:
        validresult=True

        for temp in result :

            if temp['city'] is None or temp['city'] =='0' or temp['city'] =='':
                pass
            else:
                aport={}

                aport['name'] =temp['city']
                aport['value']=temp['COUNT(*)']
                if int(temp['COUNT(*)'])>size:
                    size=int(temp['COUNT(*)'])
                portarray.append(aport)

    return portarray,count,size
