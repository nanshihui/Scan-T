#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
import portscantool
import SQLTool,config
import Sqldata
from TaskTool import TaskTool
import MySQLdb
import Sqldatatask
portscantskinstance=None
def getObject():
    global portscantskinstance
    if portscantskinstance is None:
        portscantskinstance=PortscanTask(1)
    return portscantskinstance
class PortscanTask(TaskTool):
    def __init__(self,isThread=1,deamon=True):
        TaskTool.__init__(self,isThread,deamon=deamon)
        
        self.sqlTool=Sqldatatask.getObject()
        self.connectpool=connectpool.getObject()
        self.portscan=portscantool.Portscantool()
        self.config=config.Config
        self.set_deal_num(5)
    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())

#         print req[0],req[1],req[2],req[3]
        if req[3]!='open':
            return ''
        ip=req[1]
        port=req[2]
        head=None
        ans=None
        if req[0]=='http' or req[0]=='https':
            if ip[0:4]=='http':
                address=ip+':'+port
            else:
                if  port=='443':
                    address='https'+'://'+ip+':'+port
                else:
                    
                    address=req[0]+'://'+ip+':'+port
            print address
            head,ans = self.connectpool.getConnect(address)
        else:
            head,ans=self.portscan.do_scan(ip,port,req[0])
#         print ans
#         self.sqlTool.connectdb()
        localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
        insertdata=[]
        temp=str(ans)

        insertdata.append((ip,port,localtime,str(head),str(temp)))
                                         
        extra=' on duplicate key update  detail=\''+str(temp).replace("'","&apos;")+'\' ,head=\''+str(head)+'\', timesearch=\''+localtime+'\''
        sqldatawprk=[]
        dic={"table":self.config.porttable,"select_params":['ip','port','timesearch','detail','head'],"insert_values":insertdata,"extra":extra}
        tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
        sqldatawprk.append(tempwprk)
        self.sqlTool.add_work(sqldatawprk)
#         inserttableinfo_byparams(table=self.config.porttable,select_params=['ip','port','timesearch','detail'],insert_values=insertdata,extra=extra)


#         self.sqlTool.closedb()
        print threadname+'任务结束'+str(datetime.datetime.now())
        
        
        
        
        
        return ans

if __name__ == "__main__":
    links = [ 'http://www.bunz.edu.com','http://www.baidu.com','http://www.hao123.com','http://www.cctv.com','http://www.vip.com']
    
    f = searchTask()
    f.set_deal_num(2)
    f.add_work(links)

    #f.start_task()
    while f.has_work_left():
        v,b=f.get_finish_work()
        
    while True:
        pass




