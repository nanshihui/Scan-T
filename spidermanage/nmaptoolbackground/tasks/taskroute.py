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
from ..control import usercontrol,taskscontrol,ipcontrol,portcontrol,taskcontrol

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
    #     print result
    if result:
        print '操作成功'
        response_data['result'] = '1'
    return HttpResponse(json.dumps(response_data, skipkeys=True, default=webtool.object2dict),
                        content_type="application/json")