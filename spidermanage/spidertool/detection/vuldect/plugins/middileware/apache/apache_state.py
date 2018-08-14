#coding:utf-8
import urllib2


from t import T




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url=''
        if port=='443':
            target_url = 'https://'+ip+':'+port
        else:
            
            target_url = 'http://'+ip+':'+port
        result = {}
        res=None
        result['result']=False
        vul_url = target_url + "/server-status"
        try:
            res=urllib2.urlopen(vul_url,timeout=timeout)
            res_html = res.read()
        except:
            return result
        finally:
            if res is not None:
                res.close()
                del res
        if "Server Built" in res_html:
            info = vul_url + " apache status  Vul"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='apache status Vul'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=vul_url
            result['VerifyInfo']['result'] =info
            result['VerifyInfo']['level'] = 'info'
            return result
        return result

   
            

           

if __name__ == '__main__':
    print P().verify(ip='www.apache.org',port='80')      