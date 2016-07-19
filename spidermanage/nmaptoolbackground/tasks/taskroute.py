#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.views import generic

import json
from ..model.user import User
from ..control import usercontrol,taskscontrol,ipcontrol,portcontrol,jobcontrol,taskcontrol

from spidertool import  connectpool,Sqldatatask,Sqldata,sniffertask
from spidertool import webtool


def indexpage(request):
    now = datetime.datetime.now()

    return render_to_response('index.html', {'current_date': now})
def taskshow(request):
    now = datetime.datetime.now()
    username = request.COOKIES.get('username','未知')

    return render_to_response('nmaptoolview/taskmain.html', {'username':username})
def taskquery(request):
    islogin = request.COOKIES.get('islogin',False)
    username=request.POST.get('username','')
    page=request.POST.get('page','0')
    response_data = {}
    response_data['result'] = '0'
    response_data['page']=page
    if islogin:
        response_data['result'] = '1'
        tasks,count,pagecount=taskscontrol.taskshow(username=username,page=page)
        response_data['length']=count
        response_data['jobs']=tasks
        response_data['pagecount']=pagecount
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")
    else:

        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")
def taskadd(request):
    islogin = request.COOKIES.get('islogin', False)
    username = request.COOKIES.get('username', '')
    response_data = {}
    response_data['result'] = '0'
    if islogin == False:
        print '未登录'
        return HttpResponse(json.dumps(response_data, skipkeys=True, default=webtool.object2dict),
                            content_type="application/json")
    job, result = taskscontrol.loadtask(request, username=username)
    if result == False:
        print '作业不完善'
        return HttpResponse(json.dumps(response_data, skipkeys=True, default=webtool.object2dict),
                            content_type="application/json")

    result = taskscontrol.taskadd(job)
    temp=   taskscontrol.createjob(job)
    #     print result
    if result:
        print '操作成功'
        response_data['result'] = '1'
    return HttpResponse(json.dumps(response_data, skipkeys=True, default=webtool.object2dict),
                        content_type="application/json")


def taskstart(request):

    data=updatejob(request,state='3')

    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")

def taskpause(request):
    data= updatejob(request,state='4')
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")

def taskdestroy(request):
    data=updatejob(request,state='6')
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")
def updatejob(request,state=''):
    tasktotally = taskcontrol.getObject()
    if request.method=='POST':
        islogin = request.COOKIES.get('islogin',False)
        jobid= request.POST.get('taskid','')
        username = request.COOKIES.get('username','')
        role = request.COOKIES.get('role','1')
        response_data = {}
        response_data['result'] = '0'
        if state=='3':
            tempresult = taskscontrol.jobupdate(jobstatus=state, username=username, taskid=jobid,completenum='0')
        else:

            if role=='1':
                tempresult=taskscontrol.jobupdate(jobstatus=state,username=username,taskid=jobid)
#             print 'this is user'
            else:
                tempresult=taskscontrol.jobupdate(jobstatus=state,taskid=jobid)
        if tempresult==True:

            jobs,count,pagecount=jobcontrol.jobshow(groupid=jobid)
            if count>0:


                if state == '3':
                    jobcontrol.jobupdate(jobstatus='2', groupid=jobid)
                    tasktotally.add_work(jobs)
                else:

                    jobcontrol.jobupdate(jobstatus=state, groupid=jobid)
            response_data['result'] = '1'
        return response_data
