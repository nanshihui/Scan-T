#!/usr/bin/python
#coding:utf-8
import os
from subprocess import Popen, PIPE
def rsync(ip='',port='',name=''):
    head=''
    ans=None
    keywords=''
    hackinfo=''
    import subprocess    
    p = subprocess.Popen("rsync "+ip+"::", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)    
    lines=p.stdout.readlines()
    hackinfo="".join(lines)   
    retval = p.wait() 
    if retval==0:
        keywords='rsync'
    

    return head,ans,keywords,hackinfo
