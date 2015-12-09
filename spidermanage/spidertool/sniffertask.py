#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
import  sniffertool
import webtool
from nmaptoolbackground.control import jobcontrol  
from nmaptoolbackground.model import job  
class snifferTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.sniffer= sniffertool.SniffrtTool()
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())
        jobid=req.getJobid()
        hosts=req.getJobaddress();
        ports=req.getPort()
        arguments=req.getArgument()
        isjob=req.getisJob()
        if isjob=='1':
            tempresult=jobcontrol.jobupdate(jobstatus='3',taskid=jobid,starttime=webtool.getlocaltime())
        ans = self.sniffer.scanaddress([hosts], [str(ports)], arguments)
        print threadname+'任务结束'+str(datetime.datetime.now())
        if isjob=='1':
            tempresult=jobcontrol.jobupdate(jobstatus='5',taskid=jobid,finishtime=webtool.getlocaltime())
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



