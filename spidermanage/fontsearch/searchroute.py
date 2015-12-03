#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
# from control import usercontrol,jobcontrol,ipcontrol,portcontrol,taskcontrol
from django.views import generic
from spidertool import webtool


import json


                
def indexpage(request):

    return render_to_response('fontsearchview/search.html', {'data':''})
def detailpage(request):

    return render_to_response('fontsearchview/searchdetail.html', {'data':''})
  