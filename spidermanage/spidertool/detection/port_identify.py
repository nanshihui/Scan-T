#!/usr/bin/python
#coding:utf-8
try:
    import component_func,port_func
    from plugins import port_template
    from vuldect import pocsearchtask
    from httpdect.webdection import getgeoipinfo
except Exception,e:
    print e
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

    keyword={}
    keyword['ip']=[ip]
    from spidertool import redistool
    redisresult=redistool.get(ip)
    if redisresult:
        print '从redids读取位置信息'
        keyword=redisresult
    else:
        keyword=getgeoipinfo.getGeoipinfo(keyword)
        redistool.set(ip, keyword)
        print '从redids写入位置信息'
    keyword['keywords'] = keywords
    return head,ans,keyword,hackinfo


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


