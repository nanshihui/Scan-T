#!/usr/bin/env python
# encoding: utf-8
from t import T

import requests,urllib2,json,urlparse
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        target_url = "http://"+ip+":"+str(port)+"/plugins/weathermap/editor.php"
        result = {}
        result['result']=False
        r=None
        try:
            r=requests.get(url=target_url,timeout=2)
            if r.status_code==200:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='cacti weathermap code exploit'
                result['VerifyInfo']['URL'] =ip+"/plugins/weathermap/editor.php"
                result['VerifyInfo']['payload']='IP/plugins/weathermap/editor.php'
                result['VerifyInfo']['result'] =r.text
            else:
                pass
        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
            return result
if __name__ == '__main__':
    print P().verify(ip='140.114.108.4',port='80')          
