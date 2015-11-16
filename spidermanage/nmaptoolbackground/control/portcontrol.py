#!/usr/bin/python
#coding:utf-8
from spidertool import SQLTool ,config
from ..model import port


limitpage=15
DBhelp=SQLTool.DBmanager()
localconfig=config.Config()
def portshow(ip='',port='',timesearch='',state='',name='',product='',version='',script='',page='0'):
    validresult=False
    request_params=[]
    values_params=[]
    if ip!='':
        request_params.append('ip')
        values_params.append(SQLTool.formatstring(ip))
    if port!='':
        request_params.append('port')
        values_params.append(SQLTool.formatstring(port))
    if timesearch!='':
        request_params.append('timesearch')
        values_params.append(SQLTool.formatstring(timesearch))
    if state!='':
        request_params.append('state')
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
    if script!='':
        request_params.append('script')
        values_params.append(SQLTool.formatstring(script))
    DBhelp.connectdb()
    table=localconfig.porttable
    result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['ip','port','timesearch','state','name','product','version','script'], request_params, values_params)

    if count == 0:
        pagecount = 0;
    elif count %limitpage> 0:
#         pagecount = math.ceil(count / limitpage)
        pagecount=int((count+limitpage-1)/limitpage) 


    else:
        pagecount = count / limitpage

    print pagecount
    if pagecount>0:
    
        limit='    limit  '+str(int(page)*limitpage)+','+str(limitpage)
        result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['ip','port','timesearch','state','name','product','version','script'], request_params, values_params,limit,order='port')
    
        DBhelp.closedb()
        ports=[]
        if count>0:
            validresult=True
            for temp in result :
                aport=port.Port(ip=temp[0],port=temp[1],timesearch=temp[2],state=temp[3],name=temp[4],product=temp[5],version=temp[6],script=temp[7])
                ports.append(aport)
        return ports,count,pagecount
    return [],0,pagecount
##count为返回结果行数，col为返回结果列数,count,pagecount都为int型
def loadport(request,username=''):
    jobname=request.POST.get('jobname','')
    jobaddress=request.POST.get('jobaddress','')
    jobport=request.POST.get('jobport','')
    priority=request.POST.get('priority','')
    abstract=request.POST.get('abstract','')
    tempjob=None
    if jobaddress=='' or jobname=='':
        return tempjob,False
    tempjob=job.Job(jobname=jobname,jobaddress=jobaddress,priority=priority,username=username,jobport=jobport)
    
    return tempjob,True
def portadd(port):
    nowip=port.getIP()
    vendor=port.getVendor()
    osfamily=port.getOsfamily()
    state=port.getState()
    osgen=port.getOsgen()
    updatetime=port.getUpdatetime()
    accurate=port.getAccurate()
    hostname=port.getHostname()

    
    
    
    request_params=[]
    values_params=[]
    if ip!='':
        request_params.append('ip')
        values_params.append(SQLTool.formatstring(ip))
    if port!='':
        request_params.append('port')
        values_params.append(SQLTool.formatstring(port))
    if timesearch!='':
        request_params.append('timesearch')
        values_params.append(SQLTool.formatstring(timesearch))
    if state!='':
        request_params.append('state')
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
    if script!='':
        request_params.append('script')
        values_params.append(SQLTool.formatstring(script))
    table=localconfig.porttable
    DBhelp.connectdb()

    tempresult=DBhelp.replaceinserttableinfo_byparams(table, request_params, [tuple(values_params)])
    DBhelp.closedb()

    return tempresult
def divided(ports):
    pass

    
    