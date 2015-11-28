#!/usr/bin/python
#coding:utf-8
import time
import re
from subprocess import Popen, PIPE
import os
class Zmaptool:
    def __init__(self):
        pass
# returnmsg =subprocess.call(["ls", "-l"],shell=True)
    def do_scan(self,port='80',num='10000',):
        path=os.getcwd()
        p= Popen(" ./zmap -B 10M -p "+port+" -n "+num+"  -q -O json", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')
#p= Popen(" ./zmap -B 10M -p 80 -n 100000 ", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')

        p.wait()
        retcode= p.returncode
        if retcode==0:
            returnmsg=p.stdout.read() 
            print '---------------------------------------------'
            print returnmsg
            print '---------------------------------------------'
            p = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
            list= p.findall(returnmsg)
            for i in list:
                print i
if __name__ == "__main__":
    temp=Zmaptool()
    temp.do_scan()
    












 
