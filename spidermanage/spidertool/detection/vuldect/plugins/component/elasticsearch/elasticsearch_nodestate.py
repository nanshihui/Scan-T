#!/usr/bin/env python
# encoding: utf-8
from t import T

import requests,urllib2,json,urlparse
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        target_url = "http://"+ip+":"+port+"/_nodes/stats"
        result = {}
        result['result']=False
        r=None
        try:
            r=requests.get(url=target_url,timeout=2)
            if r.status_code==200:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='information unclosed'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']='IP:port/_nodes/stats'
                result['VerifyInfo']['result'] =r.text
                result['VerifyInfo']['level'] = 'hole'
            else:
                pass
        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
                del r
            return result
if __name__ == '__main__':
    print P().verify(ip='42.120.7.120',port='9200')          
