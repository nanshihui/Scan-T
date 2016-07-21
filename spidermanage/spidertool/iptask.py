# !/usr/bin/env python
# -*- coding:utf-8 -*-
from TaskTool import TaskTool
from iptool import IPTool
from nmaptoolbackground.control import taskcontrol,jobcontrol
from nmaptoolbackground.model import job
import getLocationTool
import time,datetime
import Sqldatatask
import Sqldata
import config
iptaskinstance=None
def getObject():
    global iptaskinstance
    if iptaskinstance is None:
        iptaskinstance=IPTool(1)
    return iptaskinstance
class IPTool(TaskTool,IPTool):
    def __init__(self,isThread=1,deamon=True):
        TaskTool.__init__(self,isThread,deamon=deamon)
        

        self.set_deal_num(1)
        self.getlocationtool=getLocationTool.getObject()
        self.config=config.Config
        self.sqlTool = Sqldatatask.getObject()
    def task(self,req,threadname):
        if len(req)>2:

            startip=str(req[0])
            stopip=str(req[1])
            taskid = req[2].get('taskid','')
            taskport = req[2].get('taskport','')
            isjob = req[2].get('isjob','0')
            username=req[2].get('username','')
            command=req[2].get('command','')
            status = req[2].get('status','')

            self.getIplist(startip, stopip,taskid,taskport,isjob,username,command,status)

        ans=''
        print threadname+'执行任务中'+str(datetime.datetime.now())
        return ans

    def getIplist(self,startip,endip,taskid,taskport,isjob,username,command,status):
        ip_list = []

        res = ()
        res = self.iprange(startip,endip)
        if res < 0:
            print 'endip must be bigger than startone'
            return 
        else:
            jobs=[]
            ipsize=int(res[2])+1
            insertdata = []
            for x in xrange(ipsize):
                startipnum = self.ip2num(startip)
                startipnum = startipnum + x
                ip=self.num2ip(startipnum)


                if isjob == '0':
                    ajob = job.Job(jobaddress=str(ip), jobport='', forcesearch='0', isjob='0')
                else:
                    if command=='create':
                        ajob = job.Job(jobname=taskid, jobaddress=str(ip), username=username, groupsid=taskid,
                                   jobport=taskport, isjob='1')
                    else:
                        jobitems, count, pagecount= jobcontrol.jobshow(jobname=taskid,username=username,groupid=taskid,jobaddress=str(ip))
                        ajob = jobitems[0]



                if command=='create':
                    
                    insertdata.append((username, ajob.getJobid(), ajob.getJobname(), ajob.getPriority(), ajob.getStatus(),
                            ajob.getJobaddress(),ajob.getPort(),ajob.getCreatetime(),ajob.getForcesearch(),ajob.getGroupsid()
                            ))


                    if len(jobs) == 10 or x == ipsize - 1:
                        sqldatawprk = []
                        dic = {"table": self.config.tasktable,
                               "select_params": ['username', 'taskid', 'taskname', 'taskprior', 'taskstatus',
                                                 'taskaddress', 'taskport', 'createtime', 'forcesearch', 'groupsid'],
                               "insert_values": insertdata}
                        tempwprk = Sqldata.SqlData('inserttableinfo_byparams', dic)
                        sqldatawprk.append(tempwprk)
                        self.sqlTool.add_work(sqldatawprk)
                        sqldatawprk = []
                        insertdata=[]
                        pass
                elif command=='work':
                    self.getlocationtool.add_work([str(ip)])
                    jobs.append(ajob)



                    # updatedata = []
                    # dic = {
                    #     "table": [self.config.tasktable],
                    #     "select_params": ['taskstatus'],
                    #     "set_params": [status],
                    #     "request_params": ['groupsid'],
                    #     "equal_params": [taskid]
                    # }
                    # updateitem = Sqldata.SqlData('updatetableinfo_byparams', dic)
                    # updatedata.append(updateitem)
                    # self.sqlTool.add_work(updatedata)
                    if status=='3' or isjob=='0':
                        if len(jobs)==10 or x==ipsize-1:


                            tasktotally=taskcontrol.getObject()
                 
                            tasktotally.add_work(jobs)


                            jobs=[]
                        else:
                            pass

            setvalue="(select count(*) from taskdata where groupsid='"+str(taskid)+"')"
            dic = {
                "table": [self.config.taskstable],
                "select_params": ['num'],
                "set_params": [setvalue],
                "request_params": ['tasksid'],
                "equal_params": ['\''+str(taskid)+'\'']
            }
            updateitem = Sqldata.SqlData('updatetableinfo_byparams', dic)
            updatedata = []
            updatedata.append(updateitem)
            self.sqlTool.add_work(updatedata)
                    
if __name__ == '__main__':
    for i in xrange(3):
        print i 