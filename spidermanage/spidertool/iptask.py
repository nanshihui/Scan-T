# !/usr/bin/env python
# -*- coding:utf-8 -*-
from TaskTool import TaskTool
from iptool import IPTool
from nmaptoolbackground.control import taskcontrol
from nmaptoolbackground.model import job
import getLocationTool
import time,datetime
iptaskinstance=None
def getObject():
    global iptaskinstance
    if iptaskinstance is None:
        iptaskinstance=IPTool(1)
    return iptaskinstance
class IPTool(TaskTool,IPTool):
    def __init__(self,isThread=1,deamon=True):
        TaskTool.__init__(self,isThread,deamon=deamon)
        
#         self.portscan=portscantool.Portscantool()
        self.set_deal_num(1)
        self.getlocationtool=getLocationTool.getObject()
    def task(self,req,threadname):
        if len(req)==2:
            startip=str(req[0])
            stopip=str(req[1])
            self.getIplist(startip, stopip)

        ans=''
        print threadname+'执行任务中'+str(datetime.datetime.now())
        return ans

    def getIplist(self,startip,endip):
        ip_list = []
        res = ()
        res = self.iprange(startip,endip)
        if res < 0:
            print 'endip must be bigger than startone'
            return 
        else:
            jobs=[]
            ipsize=int(res[2])+1

            for x in xrange(ipsize):
                startipnum = self.ip2num(startip)
                startipnum = startipnum + x
                ip=self.num2ip(startipnum)
#                 self.getlocationtool.add_work([str(ip)])
                ajob=job.Job(jobaddress=str(ip),jobport='',forcesearch='0',isjob='0')

#                 tasktotally=taskcontrol.getObject()
#                 
#                 tasktotally.add_work([ajob])

                jobs.append(ajob)
                if len(jobs)==10 or x==ipsize-1:
                    tasktotally=taskcontrol.getObject()
                 
                    tasktotally.add_work(jobs)
                    time.sleep(1)
                    jobs=[]
                    
if __name__ == '__main__':
    for i in xrange(3):
        print i 