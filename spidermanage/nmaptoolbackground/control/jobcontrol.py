#!/usr/bin/python
#coding:utf-8
from spidertool import SQLTool ,config
from ..model import job


limitpage=15
DBhelp=SQLTool.DBmanager()
localconfig=config.Config()
def jobshow(jobname='',jobstatus='',username='',taskid='',jobport='',result='',page='0'):
    validresult=False
    request_params=[]
    values_params=[]
    if jobname!='':
        request_params.append('taskname')
        values_params.append(SQLTool.formatstring(jobname))
    if jobstatus!='':
        request_params.append('taskstatus')
        values_params.append(SQLTool.formatstring(jobstatus))
    if username!='':
        request_params.append('username')
        values_params.append(SQLTool.formatstring(username))
    if taskid!='':
        request_params.append('taskid')
        values_params.append(SQLTool.formatstring(taskid))
    if jobport!='':
        request_params.append('taskport')
        values_params.append(SQLTool.formatstring(jobport))
    if result!='':
        request_params.append('result')
        values_params.append(SQLTool.formatstring(result))
    DBhelp.connectdb()
    table=localconfig.tasktable
    result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['username','taskid','taskname','taskprior','taskstatus','starttime','taskaddress','taskport','result','endtime','createtime'], request_params, values_params)

    if count == 0:
        pagecount = 0;
    elif count %limitpage> 0:
#         pagecount = math.ceil(count / limitpage)
        pagecount=int((count+limitpage-1)/limitpage) 


    else:
        pagecount = count / limitpage

    print pagecount
    if pagecount>0:
    
        limit='    limit  '+str(page)+','+str(limitpage)
        result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['username','taskid','taskname','taskprior','taskstatus','starttime','taskaddress','taskport','result','endtime','createtime'], request_params, values_params,limit,order='createtime desc')
    
        DBhelp.closedb()
        jobs=[]
        if count>0:
            validresult=True
            for temp in result :
                ajob=job.Job(username=temp[0],jobid=temp[1],jobname=temp[2],priority=temp[3],jobstatus=temp[4],starttime=temp[5],jobaddress=temp[6],jobport=temp[7],result=temp[8],endtime=temp[9],createtime=temp[10])
                jobs.append(ajob)
        return jobs,count,pagecount
    return [],0,pagecount
##count为返回结果行数，col为返回结果列数,count,pagecount都为int型
def loadjob(request,username=''):
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
def jobadd(job):
    jobname=job.getJobname()
    jobaddress=job.getJobaddress()
    jobport=job.getPort()
    priority=job.getPriority()
    jobstatus=job.getStatus()
    username=job.getUsername()
    starttime=job.getStarttime()
    createtime=job.getCreatetime()
    taskid=job.getJobid()
    result=job.getResult()
    request_params=[]
    values_params=[]
    if createtime!='':
        request_params.append('createtime')
        values_params.append(createtime)
    if starttime!='':
        request_params.append('starttime')
        values_params.append(starttime)
    if jobaddress!='':
        request_params.append('taskaddress')
        values_params.append(jobaddress)
    if priority!='':
        request_params.append('taskprior')
        values_params.append(priority)
    if jobname!='':
        request_params.append('taskname')
        values_params.append(jobname)
    if jobstatus!='':
        request_params.append('taskstatus')
        values_params.append(jobstatus)
    if username!='':
        request_params.append('username')
        values_params.append(username)
    if taskid!='':
        request_params.append('taskid')
        values_params.append(taskid)
    if jobport!='':
        request_params.append('taskport')
        values_params.append(jobport)
    if result!='':
        request_params.append('result')
        values_params.append(result)
    table=localconfig.tasktable
    DBhelp.connectdb()

    tempresult=DBhelp.inserttableinfo_byparams(table, request_params, [tuple(values_params)])
    DBhelp.closedb()

    return tempresult

    
    