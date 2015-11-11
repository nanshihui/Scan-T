#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.views import generic
# Create your views here.
def indexpage(request):
    return render_to_response('nmaptoolview/mainpage.html',{})
def login(request):
    if request.method=='GET':
        return render_to_response('nmaptoolview/login.html', {'data':''})
    else:
        if request.POST.get('username','')=='123' and  request.POST.get('password','')=='123':
        
            return render_to_response('nmaptoolview/mainpage.html', {'data':'用户名和密码成功'})  
        return render_to_response('nmaptoolview/login.html', {'data':'用户名或密码错误'})  


