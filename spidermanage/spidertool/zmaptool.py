#!/usr/bin/python
#coding:utf-8
import time
import re
from subprocess import Popen, PIPE
import os
import SQLTool
import config
class Zmaptool:
    def __init__(self):
        self.sqlTool=SQLTool.DBmanager()
        self.config=config.Config
# returnmsg =subprocess.call(["ls", "-l"],shell=True)
    def do_scan(self,port='80',num='100',):
        path=os.getcwd()
#         p= Popen(" ./zmap -B  4M -p "+port+" -N "+num+"   -q -O json", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')
        
        p= Popen(" zmap -B  4M -p "+port+" -N "+num+"   -q -O json", stdout=PIPE, shell=True)
#        'sudo zmap -p 80 -B 10M -N 50 -q --output-fields=classification,saddr,daddr,sport,dport,seqnum,acknum,cooldown,repeat  -o - '+
#        '| sudo ./forge-socket -c 50 -d http-req > http-banners.out'

#p= Popen(" ./zmap -B 10M -p 80 -n 100000 ", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')

        p.wait()
        retcode= p.returncode
        if retcode==0:
            returnmsg=p.stdout.read() 
            p = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
            list= p.findall(returnmsg)
            self.sqlTool.connectdb()
            localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
            insertdata=[]
            for i in list:
                insertdata.append((str(i),port,localtime,'on'))
            extra=' on duplicate key update  state=\'on\' , timesearch=\''+localtime+'\'';
            self.sqlTool.inserttableinfo_byparams(self.config.porttable,['ip','port','timesearch','state'],insertdata,extra)
            self.sqlTool.closedb()
if __name__ == "__main__":
    temp=Zmaptool()
    temp.do_scan()
    












 
