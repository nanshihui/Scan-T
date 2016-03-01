#!/usr/bin/python
#coding:utf-8
import component_func
from plugins import port_template
def port_deal(ip='',port='',name=''):
    
#     way='sql'
#     getFunc(way,way)(way)  
    pass


def getFunc(name,port):
    func=component_func.componentFunc.get(name,port_template.empty)
#检测对应产品，使用payload检测漏洞        
    return func

way='mysql'
getFunc(way,way)(ip='',port='',name='')
