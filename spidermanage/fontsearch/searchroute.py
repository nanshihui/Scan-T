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
    username = request.COOKIES.get('username','')
    return render_to_response('fontsearchview/search.html', {'data':'','username':username})
def mainpage(request):
    content=request.GET.get('searchcontent','')
    page=request.GET.get('page','0')
    username = request.COOKIES.get('username','')
    return render_to_response('fontsearchview/searchdetail.html', {'data':content,'page':page,'username':username})
def detailpage(request):
    content=request.POST.get('content','')
    page=request.POST.get('page','0')
    username = request.COOKIES.get('username','')
    response_data = {}  
    response_data['result'] = '0'
    jsoncontent=None
    import json
    try:
        jsonmsg='{'+content+'}'
        jsoncontent=json.loads(jsonmsg)
    except Exception,e:
        print e
        pass

    if jsoncontent is None:
    
        if  content!='' and len(content)>0:
            print '存在内容，进入elasticsearch 检索'
#         extra='    or   script  like \'%'+content+'%\' or detail  like \'%'+content+'%\'  or timesearch like ' +'\'%'+content+'%\' or head like \'%' +content+'%\') and  snifferdata.ip=ip_maindata.ip '
#         ports,portcount,portpagecount=portcontrol.portabstractshow(ip=content,port=content,timesearch=content,state=content,name=content,product=content,version=content,page=page,extra=extra,command='or')
          
            import sys
            sys.path.append("..")
            from elasticsearchmanage import elastictool
            ports,portcount,portpagecount=elastictool.search(page=page,dic=None,content=content)
#             extra='     where     match(version,product,head,detail,script,hackinfo,disclosure,keywords) against(\''+content+'\' in Boolean mode)  '

#             ports,portcount,portpagecount=portcontrol.portabstractshow(page=page,extra=extra,command='or')

            print '检索完毕'
            response_data['result'] = '1' 
    
    
            response_data['ports']=ports
            response_data['portslength']=portcount
            response_data['portspagecount']=portpagecount
            response_data['portspage']=page
            response_data['username']=username
    else:
        action=jsoncontent.keys()
        if 'use' in action or 'city' in action:
            del jsoncontent['use']
            jsoncontent['page']=page
            if 'all' in action:
                
                extra='     where     match(version,product,head,detail,script,hackinfo,disclosure,keywords) against(\''+jsoncontent['all']+'\' in Boolean mode)  '

                ports,portcount,portpagecount=portcontrol.portabstractshow(page=page,extra=extra,command='or')

            else:
        
                ports,portcount,portpagecount=getattr(portcontrol, 'portabstractshow','portabstractshow')(**jsoncontent)
            response_data['result'] = '1' 
            response_data['ports']=ports
            response_data['portslength']=portcount
            response_data['portspagecount']=portpagecount
            response_data['portspage']=page
            response_data['username']=username
        else:
            if len(content)==0:
                return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")  
 
            print '进入elasticsearch 具体关键词匹配'
            import sys
            sys.path.append("..")
            from elasticsearchmanage import elastictool
            ports,portcount,portpagecount=elastictool.search(page=page,dic=jsoncontent,content=None)
            response_data['result'] = '1' 
            response_data['ports']=ports
            response_data['portslength']=portcount
            response_data['portspagecount']=portpagecount
            response_data['portspage']=page
            response_data['username']=username
    try:

        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict), content_type="application/json")
    except Exception,e:
        print e
        return HttpResponse(json.dumps(response_data,skipkeys=True,default=webtool.object2dict,encoding='latin-1'), content_type="application/json")


        # return HttpResponse(json.dumps(response_data, skipkeys=True, default=webtool.object2dict, encoding='GB2312'),
        #             content_type="application/json")

    

  