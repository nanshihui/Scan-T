#!/usr/bin/python
#coding:utf-8
import port_template
def port_deal(ip='',port='',name=''):
    
#     way='sql'
#     getFunc(way,way)(way)  
    pass


def getFunc(name,port):
    func=port_template.portFunc.get(name,port_template.empty)
#检测对应产品，使用payload检测漏洞        
    return func

way='sql'
getFunc(way,way)(way)
