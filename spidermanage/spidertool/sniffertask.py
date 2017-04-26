#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime,config
import time
import connectpool
from TaskTool import TaskTool
import  sniffertool,Sqldatatask,Sqldata
import webtool
from logger import initLog
from nmaptoolbackground.control import jobcontrol  
from nmaptoolbackground.model import job  
snifferinstance=None
def getObject():
    global snifferinstance
    if snifferinstance is None:
        snifferinstance=snifferTask(1)
        snifferinstance.set_deal_num(3)
    return snifferinstance
class snifferTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.logger = initLog('logs/sniffertask.log', 2, True,'sniffertask')
        self.sqlTool = Sqldatatask.getObject()
        self.sniffer= sniffertool.SniffrtTool(logger=self.logger)
        self.config=config.Config
    def task(self,req,threadname):
        self.logger and self.logger.info('%sNMAP 扫描执行任务中%s', threadname,str(datetime.datetime.now()))


        jobid=req.getJobid()
        jobid=str(jobid)
        hosts=req.getJobaddress();
        ports=req.getPort()
        arguments=req.getArgument()
        isjob=req.getisJob()
        if isjob=='1':
            tempresult=jobcontrol.jobupdate(jobstatus='3',taskid=str(jobid),starttime=webtool.getlocaltime())
        ans = self.sniffer.scanaddress([hosts], [str(ports)], arguments)
        self.logger and self.logger.info('%sNMAP 扫描任务结束%s', threadname,str(datetime.datetime.now()))

        if isjob=='1':
            tempresult=jobcontrol.jobupdate(jobstatus='5',taskid=str(jobid),finishtime=webtool.getlocaltime())

            setvalue = " (select count(*) from taskdata where  taskstatus=5 and groupsid= (select groupsid from taskdata where taskid='"+jobid+"'))"
            dic = {
                "table": [self.config.taskstable],
                "select_params": ['completenum'],
                "set_params": [setvalue],
                "request_params": ['tasksid'],
                "equal_params": ['(select groupsid  from taskdata where taskid=\''+jobid+'\')']
            }
            updateitem = Sqldata.SqlData('updatetableinfo_byparams', dic)
            updatedata = []
            updatedata.append(updateitem)
            statusdic={
                "table": [self.config.taskstable],
                "select_params": ['status'],
                "set_params": ['5'],
                "request_params": ['num'],
                "equal_params": ['completenum']
            }
            statusitem = Sqldata.SqlData('updatetableinfo_byparams', statusdic)
            updatedata.append(statusitem)
            self.sqlTool.add_work(updatedata)
        # ans=''
        return ans
    
if __name__ == "__main__":   
    links = []
    temp= job.Job(jobaddress='www.bnuz.edu.cn',jobport='400-800',jobname='task1')
    temp1=  job.Job(jobaddress='localhost',jobport='400-800',jobname='task2')
    temp2=  job.Job(jobaddress='www.cctv.com',jobport='400-800',jobname='task3')
    temp3=  job.Job(jobaddress='www.vip.com',jobport='400-800',jobname='task4')
    links.append(temp)
    links.append(temp1)
    links.append(temp2)
    links.append(temp3)
    S_produce= snifferTask(1)#表示创建的是线程
    S_produce.set_deal_num(10)
    starttime = datetime.datetime.now()



    S_produce.add_work(links)
#     while S_produce.has_work_left():
#         a,b=S_produce.get_finish_work()
    endtime = datetime.datetime.now()

    print (endtime - starttime).seconds
#   print b



