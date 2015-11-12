#!/usr/bin/python
#coding:utf-8
from spidertool import SQLTool ,config
 
DBhelp=SQLTool.DBmanager()
localconfig=config.Config()
def validuser(username,password):
    validresult=False
    DBhelp.connectdb()
    print localconfig.usertable
    result,content,count,col=DBhelp.searchtableinfo_byparams([localconfig.usertable], ['username','role','userpower'], ['username','password'], [SQLTool.formatstring(username),SQLTool.formatstring(password)])
    DBhelp.closedb()
    if col>0:
        validresult=True
        for temp in result:
             print str(temp[0])+str(temp[1])+str(temp[2])
    
    return validresult,1,1,1
    