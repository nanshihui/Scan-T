#!/usr/bin/python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.views import generic

from model.user import User
from control import usercontrol,jobcontrol,ipcontrol,portcontrol,taskcontrol
from spidertool import  connectpool,Sqldatatask,Sqldata,sniffertask
from spidertool import webtool
import httplib
import json

# Create your views here.
#a function to change the state of job
def userinfo(request):
    
    return render_to_response('nmaptoolview/userinfo.html', {'data':''})

def destroyjob(request):
    data=updatejob(request,state='6')
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
def pausejob(request):
    data= updatejob(request,state='4')
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
def startjob(request):
    data=updatejob(request,state='2')
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
#a function to get the port information of IP
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
#a function to get the job of user
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
#             print 'this is user'
        else:
            jobs,count,pagecount=jobcontrol.jobshow(taskid=jobid)
#             print 'this is administor'
        if count>0 and jobid!='':
            ip=jobs[0].getJobaddress()   
            port=jobs[0].getPort()
            statuss=jobs[0].getStatus()
            isip=webtool.isip(ip)
            if isip:
                
                ips,counts,pagecounts=ipcontrol.ipshow(ip=ip)
            else:
                ips,counts,pagecounts=ipcontrol.ipshow(hostname=ip)
                if counts>0:
                    ip=ips[0].getIP()
                else:
                    ip='未知'
            response_data['result'] = '1' 
            response_data['ipstate'] = '0' 
            response_data['ip']=ip
            response_data['jobstate']=statuss
#             print 'it has this task'
            if counts>0:
#                 print 'it has this ip'
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

#a function to redirect to main page               
def indexpage(request):
    islogin = request.COOKIES.get('islogin',False)
    username = request.COOKIES.get('username','')

    if islogin:
        return render_to_response('nmaptoolview/taskmain.html',{'username':username})
    return render_to_response('nmaptoolview/login.html', {'data':''})
def groupitem(request):
    islogin = request.COOKIES.get('islogin',False)
    username = request.COOKIES.get('username','')
    groupid= request.GET.get('groupid','')
    if islogin:
        return render_to_response('nmaptoolview/mainpage.html',{'username':username,'groupid':groupid})
    return render_to_response('nmaptoolview/login.html', {'data':''})
def chartshow(request):
    response= render_to_response('nmaptoolview/chartshow.html', {'data':''})
    return response
#a function to redirect to get the test data from baidu
def chartdata(request):
    httpClient = None
    response_data={}
    try:
#         httpClient = httplib.HTTPConnection('echarts.baidu.com', 80, timeout=30)
#         httpClient.request('GET', '/doc/example/data/migration.json')
        connectpool_t=connectpool.getObject()
        address='http://echarts.baidu.com/echarts2/doc/example/data/migration.json'
        head,ans = connectpool_t.getConnect(address)
    #response是HTTPResponse对象
#         response = httpClient.getresponse()
#         print response.status
#         print response.reason
        response_data= ans
        print response_data
    except Exception, e:
        print '接受的数据出现异常'+str(e)
    finally:
        if httpClient:
            httpClient.close()
#         print response_data
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict),  content_type="application/json")      
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
            response = render_to_response('nmaptoolview/taskmain.html', {'data':'用户名和密码成功','username':username})
            loginuser=User(result,username,password,role,power)
#将username写入浏览器cookie,失效时间为3600

            webtool.setCookies(response,loginuser,3600)

            return response
        else:
            return render_to_response('nmaptoolview/login.html', {'data':'用户名或密码错误'})  
#a function to get the job
def sigin(request):
    if request.method=='GET':
        return render_to_response('nmaptoolview/sigin.html', {'data':''})
    
    
def jobshow(request):

    islogin = request.COOKIES.get('islogin',False)
    username=request.POST.get('username','')
    page=request.POST.get('page','0')
    groupid = request.POST.get('groupid', '')

    response_data = {}  
    response_data['result'] = '0' 
    response_data['page']=page
    if islogin:
        response_data['result'] = '1' 
        jobs,count,pagecount=jobcontrol.jobshow(username=username,page=page,groupid=groupid)
        response_data['length']=count
        response_data['jobs']=jobs
        response_data['pagecount']=pagecount
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")
    else:

        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")



#a function to add the job
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
#     print result
    if result:
        print '操作成功'
        response_data['result'] = '1' 
    return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
def updatejob(request,state=''):
    if request.method=='POST':
        islogin = request.COOKIES.get('islogin',False)
        jobid= request.POST.get('taskid','')
        username = request.COOKIES.get('username','') 
        role = request.COOKIES.get('role','1')
        response_data = {}  
        response_data['result'] = '0' 
        if role=='1':
            tempresult=jobcontrol.jobupdate(jobstatus=state,username=username,taskid=jobid)
#             print 'this is user'
        else:
            tempresult=jobcontrol.jobupdate(jobstatus=state,taskid=jobid)
        if tempresult==True:
            if state=='2':
                jobs,count,pagecount=jobcontrol.jobshow(taskid=jobid)
                if count>0:
                    tasktotally=taskcontrol.getObject()
                    if jobs[0].getForcesearch==1:


                        tasktotally.add_work(jobs)
                    else:

                        tasktotally.add_work(jobs)
                        
            response_data['result'] = '1'
        return response_data
    
    
    
#the function below is to use for assign work to other PC   
def getwork(request):
    data={}
    taskinstance=sniffertask.getObject()
    tempwork=taskinstance.get_work()
    
    if len(tempwork)>0:
        data['result']='1'
        data['jobs']=tempwork
    else:
        data['result']='0'
    
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")   

def upload_ip_info(request):
    sqldatawprk=[]
    func=request.POST.get('func','')
    dic=request.POST.get('dic','{}')
    nowdic=eval(dic)#存在安全隐患, 改用json库
    tempwprk=Sqldata.SqlData(func,nowdic)
    sqldatawprk.append(tempwprk)
    sqlTool=Sqldatatask.getObject()
    sqlTool.add_work(sqldatawprk)
#     works=request.POST.get('workdetail',[])
#     print works
#     tempvendor=request.POST.get('vendor','')
#     temposfamily=request.POST.get('osfamily','')
#     temposgen=request.POST.get('osgen','')
#     tempaccuracy=request.POST.get('accuracy','')
#     temphostname=request.POST.get('hostname','')
#     tempstate=request.POST.get('state','')
#     ipcontrol.ip_info_upload(temphosts,tempvendor,temposfamily,temposgen,tempaccuracy,localtime,temphostname,tempstate)
    data={}
    data['result']='1'
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")   

def upload_port_info(request):
    sqldatawprk=[]
    func=request.POST.get('func','')
    dic=request.POST.get('dic','{}')
    nowdic=eval(dic)
    tempwprk=Sqldata.SqlData(func,nowdic)
    sqldatawprk.append(tempwprk)
    sqlTool=Sqldatatask.getObject()
    sqlTool.add_work(sqldatawprk)

    data={}
    data['result']='1'
    return HttpResponse(json.dumps(data,skipkeys=True,default=webtool.object2dict), content_type="application/json")   

def systeminfo(request):
    from spidertool import sniffertask, zmaptool,portscantask,Sqldatatask
    from spidertool.detection.fluzzdetect import fuzztask
    from spidertool.detection.vuldect import pocsearchtask
    resultdata={}
    resultdata['nmapfont']=taskcontrol.getObject().get_length()
    resultdata['nmapfont_running'] = taskcontrol.getObject().get_current_task_num()
    resultdata['nmapback']=sniffertask.getObject().get_length()
    resultdata['nmapback_running'] = sniffertask.getObject().get_current_task_num()
    resultdata['portacsn']=portscantask.getObject().get_length()
    resultdata['portacsn_running'] = portscantask.getObject().get_current_task_num()
    resultdata['fuzz']=fuzztask.getObject().get_length()
    resultdata['fuzz_running'] = fuzztask.getObject().get_current_task_num()
    resultdata['pocdect'] = pocsearchtask.getObject().get_length()
    resultdata['pocdect_running']=pocsearchtask.getObject().get_current_task_num()
    resultdata['sqltask'] = Sqldatatask.getObject().get_length()
    resultdata['sqltask_running']=Sqldatatask.getObject().get_current_task_num()
    return HttpResponse(json.dumps(resultdata,skipkeys=True,default=webtool.object2dict), content_type="application/json")