#!/usr/bin/python
#coding:utf-8
from spidertool import SQLTool ,config,Sqldatatask
from ..model import ipmain
import time 
limitpage=15

localconfig=config.Config()
def ipshow(ip='',vendor='',osfamily='',osgen='',accurate='',updatetime='',hostname='',state='',page='0',city=''):
    validresult=False
    request_params=[]
    values_params=[]
    if ip!='':
        request_params.append('ip')
        values_params.append(SQLTool.formatstring(ip))
    if vendor!='':
        request_params.append('vendor')
        values_params.append(SQLTool.formatstring(vendor))
    if osfamily!='':
        request_params.append('osfamily')
        values_params.append(SQLTool.formatstring(osfamily))
    if osgen!='':
        request_params.append('osgen')
        values_params.append(SQLTool.formatstring(osgen))
    if accurate!='':
        request_params.append('accurate')
        values_params.append(SQLTool.formatstring(accurate))
    if updatetime!='':
        request_params.append('updatetime')
        values_params.append(SQLTool.formatstring(updatetime))
    if hostname!='':
        request_params.append('hostname')
        values_params.append(SQLTool.formatstring(hostname))
    if state!='':
        request_params.append('state')
        values_params.append(SQLTool.formatstring(state))
    if city!='':
        request_params.append('city')
        values_params.append(SQLTool.formatstring(city))
    DBhelp=SQLTool.DBmanager()
    DBhelp.connectdb()
    table=localconfig.iptable
    result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['ip','vendor','osfamily','osgen','accurate','updatetime','hostname','state','city'], request_params, values_params)

    if count == 0:
        pagecount = 0;
    elif count %limitpage> 0:
#         pagecount = math.ceil(count / limitpage)
        pagecount=int((count+limitpage-1)/limitpage) 


    else:
        pagecount = count / limitpage

#     print str(pagecount)+'当前页数'
    if pagecount>0:
    
        limit='    limit  '+str(int(page)*limitpage)+','+str(limitpage)
        result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['ip','vendor','osfamily','osgen','accurate','updatetime','hostname','state','city'], request_params, values_params,limit,order='updatetime desc')
    
        DBhelp.closedb()
        ips=[]
        if count>0:
            validresult=True
            for temp in result :
                aip=ipmain.Ip(ip=temp['ip'],vendor=temp['vendor'],osfamily=temp['osfamily'],osgen=temp['osgen'],accurate=temp['accurate'],updatetime=temp['updatetime'],hostname=temp['hostname'],state=temp['state'],city=temp['city'])
#                 aip=ipmain.Ip(ip=temp[0],vendor=temp[1],osfamily=temp[2],osgen=temp[3],accurate=temp[4],updatetime=temp[5],hostname=temp[6],state=temp[7])
                ips.append(aip)
        return ips,count,pagecount
    return [],0,pagecount
##count为返回结果行数，col为返回结果列数,count,pagecount都为int型

def ipadd(ip):
    nowip=ip.getIP()
    vendor=ip.getVendor()
    osfamily=ip.getOsfamily()
    state=ip.getState()
    osgen=ip.getOsgen()
    updatetime=ip.getUpdatetime()
    accurate=ip.getAccurate()
    hostname=ip.getHostname()

    
    
    
    request_params=[]
    values_params=[]
    if nowip!='':
        request_params.append('ip')
        values_params.append(nowip)
    if vendor!='':
        request_params.append('vendor')
        values_params.append(vendor)
    if osfamily!='':
        request_params.append('osfamily')
        values_params.append(osfamily)
    if state!='':
        request_params.append('state')
        values_params.append(state)
    if osgen!='':
        request_params.append('osgen')
        values_params.append(osgen)
    if updatetime!='':
        request_params.append('updatetime')
        values_params.append(updatetime)
    if accurate!='':
        request_params.append('accurate')
        values_params.append(accurate)
    if hostname!='':
        request_params.append('hostname')
        values_params.append(hostname)
    if city!='':
        request_params.append('city')
        values_params.append(city)
    table=localconfig.iptable
    DBhelp=SQLTool.DBmanager()
    DBhelp.connectdb()

    tempresult=DBhelp.replaceinserttableinfo_byparams(table, request_params, [tuple(values_params)])
    DBhelp.closedb()

    return tempresult
def ip_info_upload(temphosts,tempvendor,temposfamily,temposgen,tempaccuracy,localtime,temphostname,tempstate):
    localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
    sqlTool=Sqldatatask.getObject()
#     sqldatawprk=[]
#     dic={"table":self.config.iptable,"select_params": ['ip','vendor','osfamily','osgen','accurate','updatetime','hostname','state'],"insert_values": [(temphosts,tempvendor,temposfamily,temposgen,tempaccuracy,localtime,temphostname,tempstate)]}
#     tempwprk=Sqldata.SqlData('replaceinserttableinfo_byparams',dic)
#     sqldatawprk.append(tempwprk)
#     sqlTool.add_work(sqldatawprk)
    pass 
    
    