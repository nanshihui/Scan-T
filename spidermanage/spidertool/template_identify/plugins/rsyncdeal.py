#!/usr/bin/python
#coding:utf-8
# import os
# from subprocess import Popen, PIPE
# import sys
# sys.path.append("..")
from spidertool import commandtool
def rsync(ip='',port='',name='',productname=''):
    head=''
    ans=None
    keywords=''
    hackinfo=''
    p=None
#     import subprocess    
#     p = subprocess.Popen("rsync "+ip+"::", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)    
#     lines=p.stdout.readlines()
#     hackinfo="".join(lines)   
    usecommand="rsync "+ip+"::"
    result=''
    try:  
        result = commandtool.command(usecommand,timeout=10)
    except commandtool.TimeoutError,e:  
        hackinfo=str(e) 
    else:  
        hackinfo='command:'+usecommand+'\nresult:'+result 
        keywords='rsync'

    print ip+hackinfo

    return head,ans,keywords,hackinfo
# rsync(ip='121.40.217.83')
# rsync(ip='202.100.78.10')121.40.217.83
