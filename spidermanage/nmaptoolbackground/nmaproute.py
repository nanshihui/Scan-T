#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from control import usercontrol
from django.views import generic
# Create your views here.
def indexpage(request):
    return render_to_response('nmaptoolview/mainpage.html',{})
def login(request):
    if request.method=='GET':
        return render_to_response('nmaptoolview/login.html', {'data':''})
    else:
        username=request.POST.get('username','')
        password=request.POST.get('password','')

        result,username,role,power= usercontrol.validuser(username,password)
        return render_to_response('nmaptoolview/mainpage.html', {'data':'用户名和密码成功'})  
        return render_to_response('nmaptoolview/login.html', {'data':'用户名或密码错误'})  


