#!/usr/bin/python
#coding:utf-8
import component_func,port_func
from plugins import port_template
from poc_file import pocsearchtask
def port_deal(ip='',port='',name='',productname='',head=None,context=None,nmapscript=None):
    head=None
    ans=None
    keywords=name
    hackinfo=''
    port_function=getFunc(name,port,productname)
    if port_function !=None:
        head,ans,keywords,hackinfo=port_function(ip=ip,port=port,name=name,productname=productname)
    else:
        temp=pocsearchtask.getObject()
        temp.add_work([(head,context,ip,port,productname,keywords,nmapscript,name)])
    return head,ans,keywords,hackinfo


def getFunc(name,port,productname):
    func=None
    if name !='':
        
        func=component_func.componentFunc.get(name,None)
    if str(port) !='':
        func=port_func.portFunc.get(str(port),None)
    else:
        func= None
#检测对应产品，使用payload检测漏洞        
    return func


