#!/usr/bin/python
#coding:utf-8
import component_func,port_func
from plugins import port_template
def port_deal(ip='',port='',name='',productname=''):
    head=None
    ans=None
    keywords=name
    hackinfo=''
    port_function=getFunc(name,port,productname)
    if port_function !=None:
        head,ans,keywords,hackinfo=port_function(ip=ip,port=port,name=name,productname=productname)
        
    return head,ans,keywords,hackinfo


def getFunc(name,port,productname):
    func=None
    if name !='':
        
        func=component_func.componentFunc.get(name,port_template.empty)
    if str(port) !='':
        func=port_func.portFunc.get(str(port),port_template.empty)
    else:
        func= None
#检测对应产品，使用payload检测漏洞        
    return func


