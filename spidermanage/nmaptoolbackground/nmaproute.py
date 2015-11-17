#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from control import usercontrol,jobcontrol,ipcontrol,portcontrol
from django.views import generic
from spidertool import webtool
from model.user import User

import json
# Create your views here.
def destroyjob(request):
    if request.method=='POST':
        islogin = request.COOKIES.get('islogin',False)
        jobid= request.POST.get('taskid','')
        username = request.COOKIES.get('username','') 
        role = request.COOKIES.get('role','1')
        response_data = {}  
        response_data['result'] = '0' 
        if role=='1':
            tempresult=jobcontrol.jobupdate(jobstatus='6',username=username,taskid=jobid)
            print 'this is user'
        else:
            tempresult=jobcontrol.jobupdate(jobstatus='6',taskid=jobid)
        if tempresult==True:
            response_data['result'] = '1'
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
def pausejob(request):
    if request.method=='POST':
        islogin = request.COOKIES.get('islogin',False)
        jobid= request.POST.get('taskid','')
        username = request.COOKIES.get('username','') 
        role = request.COOKIES.get('role','1')
        response_data = {}  
        response_data['result'] = '0' 
        if role=='1':
            tempresult=jobcontrol.jobupdate(jobstatus='4',username=username,taskid=jobid)
            print 'this is user'
        else:
            tempresult=jobcontrol.jobupdate(jobstatus='4',taskid=jobid)
        if tempresult==True:
            response_data['result'] = '1'
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
def startjob(request):
    if request.method=='POST':
        islogin = request.COOKIES.get('islogin',False)
        jobid= request.POST.get('taskid','')
        username = request.COOKIES.get('username','') 
        role = request.COOKIES.get('role','1')
        response_data = {}  
        response_data['result'] = '0' 
        if role=='1':
            tempresult=jobcontrol.jobupdate(jobstatus='2',username=username,taskid=jobid)
            print 'this is user'
        else:
            tempresult=jobcontrol.jobupdate(jobstatus='2',taskid=jobid)
        if tempresult==True:
            response_data['result'] = '1'
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
def taskdetail(request):
    if request.method=='GET':
        islogin = request.COOKIES.get('islogin',False)
        jobid= request.GET.get('jobid','')
        username = request.COOKIES.get('username','')
        role = request.COOKIES.get('role','1')
        if islogin==False:
            return render_to_response('nmaptoolview/login.html', {'data':''})
        if role=='1':
            jobs,count,pagecount=jobcontrol.jobshow(username=username,taskid=jobid)
        else:
            jobs,count,pagecount=jobcontrol.jobshow(taskid=jobid)
        if count>0 and jobid!='':
            return render_to_response('nmaptoolview/taskdetail.html', {'taskid':jobid,'username':username})
        else:
            return HttpResponse("权限不足或者没有此任务")

            

#     jobcontrol.getIP(jobs)
def ipmain(request):   
    if request.method=='POST':
        islogin = request.COOKIES.get('islogin',False)
        jobid= request.POST.get('taskid','')
        page= request.POST.get('page','0')
        username = request.COOKIES.get('username','') 
        role = request.COOKIES.get('role','1')
        response_data = {}  
        response_data['result'] = '0' 
        if role=='1':
            jobs,count,pagecount=jobcontrol.jobshow(username=username,taskid=jobid)
            print 'this is user'
        else:
            jobs,count,pagecount=jobcontrol.jobshow(taskid=jobid)
            print 'this is administor'
        if count>0 and jobid!='':
            ip=jobs[0].getJobaddress()   
            port=jobs[0].getPort()
            statuss=jobs[0].getStatus()
            
            ips,counts,pagecounts=ipcontrol.ipshow(ip=ip)
            response_data['result'] = '1' 
            response_data['ipstate'] = '0' 
            response_data['ip']=ip
            response_data['jobstate']=statuss
            print 'it has this task'
            if counts>0:
                print 'it has this ip'
                response_data['ipstate'] = '1' 
                response_data['length']=counts
                response_data['ips']=ips[0]
                response_data['pagecount']=pagecounts
                portinfo=portcontrol.divided(port,'port')
                ports,portcount,portpagecount=portcontrol.portshow(ip=ip,page=page,extra=portinfo)
                response_data['ports']=ports
                response_data['portslength']=portcount
                response_data['portspagecount']=portpagecount
                response_data['portspage']=page
                return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
            else:
                return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  

        else:
            return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  

                
def indexpage(request):
    islogin = request.COOKIES.get('islogin',False)
    username = request.COOKIES.get('username','')
    if islogin:
        return render_to_response('nmaptoolview/mainpage.html',{'username':username})
    return render_to_response('nmaptoolview/login.html', {'data':''})
def logout(request):
    response= render_to_response('nmaptoolview/login.html', {'data':''})
    webtool.delCookies(response)
    return response
def login(request):
    if request.method=='GET':
        return render_to_response('nmaptoolview/login.html', {'data':''})
    else:
        username=request.POST.get('username','')
        password=request.POST.get('password','')

        result,username,role,power= usercontrol.validuser(username,password)
        if result:
            response = render_to_response('nmaptoolview/mainpage.html', {'data':'用户名和密码成功','username':username})  
            loginuser=User(result,username,password,role,power)
#将username写入浏览器cookie,失效时间为3600

            webtool.setCookies(response,loginuser,3600)

            return response
        else:
            return render_to_response('nmaptoolview/login.html', {'data':'用户名或密码错误'})  

def jobshow(request):

    islogin = request.COOKIES.get('islogin',False)
    username=request.POST.get('username','')
    page=request.POST.get('page','0')
    response_data = {}  
    response_data['result'] = '0' 
    response_data['page']=page
    if islogin:
        response_data['result'] = '1' 
        jobs,count,pagecount=jobcontrol.jobshow(username=username,page=page)
        response_data['length']=count
        response_data['jobs']=jobs
        response_data['pagecount']=pagecount
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
    else:
        
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
def jobadd(request):
    islogin = request.COOKIES.get('islogin',False)
    username = request.COOKIES.get('username','')
    response_data = {}  
    response_data['result'] = '0' 
    if islogin ==False:
        print '未登录'
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
    job,result=jobcontrol.loadjob(request,username=username)
    if result==False:
        print '作业不完善'
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
 
    result=jobcontrol.jobadd(job)
    print result
    if result:
        print '操作成功'
        response_data['result'] = '1' 
    return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  



    




