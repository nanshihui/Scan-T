#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
import portscantool
import SQLTool,config
from TaskTool import TaskTool

from logger import initLog
portscantskinstance=None
def getObject():
    global portscantskinstance
    if portscantskinstance is None:
        portscantskinstance=PortscanTask(1)
    return portscantskinstance
class PortscanTask(TaskTool):
    def __init__(self,isThread=1,deamon=True):
        TaskTool.__init__(self,isThread,deamon=deamon)
        import Sqldatatask
        self.logger = initLog('logs/portScantask.log', 2, True,'portscantask')
        self.sqlTool=Sqldatatask.getObject()
        self.connectpool=connectpool.getObject()
        self.portscan=portscantool.Portscantool()
        self.config=config.Config
        self.set_deal_num(15)
    def task(self,req,threadname):
        self.logger and self.logger.info('%s 端口扫描　执行任务中%s', threadname,str(datetime.datetime.now()))
#         print req[0],req[1],req[2],req[3]

        if req[3]!='open':
            return ''
        ip=req[1]
        port=req[2]
        productname=req[4]
        nmapscript=req[5]
        head=None
        ans=None
        hackinfo=''
        keywords=''

        if (req[0]=='http' or req[0]=='https') or (req[0] in ['tcpwrapped','None'] and port in ['80','8080','7001']):

            if ip[0:4]=='http':
                address=ip+':'+port
            else:
                if  port=='443':
                    address='https'+'://'+ip+':'+port

                else:
                    if req[0]=='tcpwrapped' and port in ['80','8080','7001']:
                        address = 'http://' + ip + ':' + port
                    else:
                        address=req[0]+'://'+ip+':'+port


            head,ans = self.connectpool.getConnect(address)
            try:
                from detection import page_identify

                keywords,hackinfo=page_identify.identify_main(head=head,context=ans,ip=ip,port=port,productname=productname,protocol=req[0],nmapscript=nmapscript)
            except:
                pass
        else:
            head,ans,keywords,hackinfo=self.portscan.do_scan(head=head,context=ans,ip=ip,port=port,name=req[0],productname=productname,nmapscript=nmapscript)
            pass
#         print ans
#         self.sqlTool.connectdb()
        localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
        insertdata=[]
        temp=str(ans)

        head=SQLTool.escapewordby('{'+head+'}')
        msg=SQLTool.escapewordby('{'+temp+'}')
        hackinfomsg=SQLTool.escapewordby(hackinfo)
        keywords=SQLTool.escapewordby(keywords)
        import Sqldata
        insertdata.append((ip,port,localtime,msg,str(head),str(port),hackinfomsg,keywords))
                                         
        extra=' on duplicate key update  detail=\''+msg+'\' ,head=\''+str(head)+'\', timesearch=\''+localtime+'\',hackinfo=\''+hackinfomsg+'\',keywords=\''+str(keywords)+'\''
        sqldatawprk=[]
        dic={"table":self.config.porttable,"select_params":['ip','port','timesearch','detail','head','portnumber','hackinfo','keywords'],"insert_values":insertdata,"extra":extra}
        tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
        sqldatawprk.append(tempwprk)
        self.sqlTool.add_work(sqldatawprk)
#         inserttableinfo_byparams(table=self.config.porttable,select_params=['ip','port','timesearch','detail'],insert_values=insertdata,extra=extra)


#         self.sqlTool.closedb()
       
        
        self.logger and self.logger.info('%s 端口扫描　任务结束%s', threadname,str(datetime.datetime.now()))

        
        
        
        return ans

if __name__ == "__main__":
    links = [('http','218.28.144.77','80','open','weblogic','weblogic')]
    
    f = PortscanTask()

    f.add_work(links)


        
    while True:
        pass




