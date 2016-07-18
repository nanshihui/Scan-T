#!/usr/bin/python
#coding:utf-8
from spidertool import SQLTool ,config
from ..model import tasks


limitpage=15


localconfig=config.Config()
def taskshow(taskname='',tasktatus='',username='',taskid='',taskport='',result='',page='0'):
    validresult=False
    request_params=[]
    values_params=[]
    if taskname!='':
        request_params.append('tasksname')
        values_params.append(SQLTool.formatstring(taskname))
    if tasktatus!='':
        request_params.append('status')
        values_params.append(SQLTool.formatstring(tasktatus))
    if username!='':
        request_params.append('username')
        values_params.append(SQLTool.formatstring(username))
    if taskid!='':
        request_params.append('tasksid')
        values_params.append(SQLTool.formatstring(taskid))
    if taskport!='':
        request_params.append('taskport')
        values_params.append(SQLTool.formatstring(taskport))

    DBhelp=SQLTool.DBmanager()
    DBhelp.connectdb()
    table=localconfig.taskstable
    result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['count(*)'], request_params, values_params)
    if count>0:
        count= int(result[0]['count(*)'])
    if count == 0:
        pagecount = 0;
    elif count %limitpage> 0:

        pagecount=int((count+limitpage-1)/limitpage)


    else:
        pagecount = count / limitpage

    if pagecount>0:

        limit='    limit  '+str(int(page)*limitpage)+','+str(limitpage)
        result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['username','tasksid','tasksname','status','starttime','tasksaddress','taskport','endtime','createtime','num','completenum'], request_params, values_params,limit,order='createtime desc')

        DBhelp.closedb()
        jobs=[]
        if count>0:
            validresult=True
            for temp in result :
                ajob=tasks.Tasks(username=temp['username'],tasksid=temp['tasksid'],tasksname=temp['tasksname'],taskstatus=temp['status'],starttime=temp['starttime'],taskaddress=temp['tasksaddress'],tasksport=temp['taskport'],endtime=temp['endtime'],createtime=temp['createtime'],num=temp['num'],completenum=temp['completenum'])


                jobs.append(ajob)
        return jobs,count,pagecount
    return [],0,pagecount


def loadtask(request,username=''):
    tasksname=request.POST.get('jobname','')
    taskaddress=request.POST.get('jobaddress','')
    tasksport=request.POST.get('jobport','')
    priority=request.POST.get('priority','')
    abstract=request.POST.get('abstract','')
    forcesearch=request.POST.get('forcesearch','0')
    tempjob=None
    if taskaddress=='' or tasksname=='':
        return tempjob,False
    tempjob=tasks.Tasks(tasksname=tasksname,taskaddress=taskaddress,username=username,tasksport=tasksport,forcesearch=forcesearch)

    return tempjob,True
def taskadd(job):
    jobname=job.getJobname()
    jobaddress=job.getJobaddress()
    jobport=job.getPort()

    jobstatus=job.getStatus()
    username=job.getUsername()
    starttime=job.getStarttime()
    createtime=job.getCreatetime()
    taskid=job.getJobid()

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


    table=localconfig.tasktable
    DBhelp=SQLTool.DBmanager()
    DBhelp.connectdb()

    tempresult=DBhelp.inserttableinfo_byparams(table=table, select_params=request_params,insert_values= [tuple(values_params)])

    DBhelp.closedb()

    return tempresult

def jobupdate(taskid='',jobport='',jobaddress='',jobname='',priority='',jobstatus='',starttime='',result='',username='',finishtime=''):


    request_params=[]
    values_params=[]
    wset_params=[]
    wand_params=[]
    if starttime!='':
        request_params.append('starttime')
        values_params.append(SQLTool.formatstring(starttime))
    if finishtime!='':
        request_params.append('endtime')
        values_params.append(SQLTool.formatstring(finishtime))
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
    if jobport!='':
        request_params.append('taskport')
        values_params.append(jobport)
    if result!='':
        request_params.append('result')
        values_params.append(result)
    if username!='':
        wset_params.append('username')
        wand_params.append(SQLTool.formatstring(username))
    if taskid!='':
        wset_params.append('taskid')
        wand_params.append(SQLTool.formatstring(taskid))
    table=localconfig.tasktable
    DBhelp=SQLTool.DBmanager()
    DBhelp.connectdb()

    tempresult=DBhelp.updatetableinfo_byparams([table],request_params,values_params,wset_params,wand_params)
    DBhelp.closedb()

    return tempresult







##count为返回结果行数，col为返回结果列数,count,pagecount都为int型
if __name__ == "__main__":
    tasks, count, pagecount = taskshow(username='admin', page='0')
    print tasks, count, pagecount