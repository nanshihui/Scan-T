#!/usr/bin/python
#coding:utf-8
import uuid
from spidertool import webtool
class Tasks(object):
    def __init__(self,tasksname='',taskaddress='',priority='1',starttime='',username='',tasksport='',taskstatus='1',tasksid='',result='',endtime='',createtime='',argument='',forcesearch='',isjob='1',num='',completenum=''):
        '''
        Constructor
        '''
#         taskstatus=1 //未启动
#         taskstatus=2 //排队中
#         taskstatus=3 //正在进行
#         taskstatus=4 //挂起
#         taskstatus=5 //已完成
#         taskstatus=6 //已终止
#         mode=1//正常状态
#         mode=0//异常状态
        self.tasksname=tasksname
        self.taskaddress=taskaddress
        self.priority=priority
        self.starttime=starttime
        self.username=username
        self.completenum=completenum
        self.num=num
        self.isjob=isjob
        self.mode=1
        if forcesearch!='':
            self.forcesearch=forcesearch

        else:
            self.forcesearch='0'
        if createtime!='':
            self.createtime=createtime
        else:
            self.createtime=webtool.getlocaltime()
        if tasksid!='':
            self.tasksid=tasksid
        else:
            self.tasksid=uuid.uuid1()
        self.tasksport=tasksport
        self.taskstatus=taskstatus
        self.result=result
        self.endtime=endtime
        self.argument=argument
    def setMode(self,mode):
        self.mode=mode
    def getMode(self):

        return self.mode
    def setPriority(self,priority):
        self.priority=priority
    def setArgument(self,argument):
        self.argument=argument

    def setResult(self,result):
        self.result=result
    def settaskstatus(self,taskstatus):
        self.taskstatus=taskstatus
    def getForcesearch(self):
        return self.forcesearch
    def getUsername(self):
        return self.username
    def getTasksname(self):
        return self.tasksname
    def getTaskaddress(self):
        return self.taskaddress
    def getTasksid(self):
        return self.tasksid
    def getResult(self):
        return self.result
    def getPort(self):
        return self.tasksport
    def getPriority(self):
        return self.priority
    def getisJob(self):
        return self.isjob
    def getStatus(self):
        return self.taskstatus
    def getStarttime(self):
        return self.starttime
    def getCreatetime(self):
        return self.createtime
    def getArgument(self):
        return self.argument
