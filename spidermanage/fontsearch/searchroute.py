#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from nmaptoolbackground.control import usercontrol,jobcontrol,ipcontrol,portcontrol,taskcontrol
from django.views import generic
from spidertool import webtool


import json


                
def indexpage(request):

    return render_to_response('fontsearchview/search.html', {'data':''})
def mainpage(request):
    content=request.GET.get('searchcontent','')
    
    return render_to_response('fontsearchview/searchdetail.html', {'data':content})
def detailpage(request):
    content=request.POST.get('content','')
    page=request.POST.get('page','0')
    response_data = {}  
    response_data['result'] = '0'
    print content
    if  content!='':
        extra='    or   script  like \'%'+content+'%\' or detail  like \'%'+content+'%\''
        ports,portcount,portpagecount=portcontrol.portshow(ip=content,port=content,timesearch=content,state=content,name=content,product=content,version=content,page=page,extra=extra,command='or')

        response_data['result'] = '1' 
    
    
        response_data['ports']=ports
        response_data['portslength']=portcount
        response_data['portspagecount']=portpagecount
        response_data['portspage']=page
    return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
    
    
    

  