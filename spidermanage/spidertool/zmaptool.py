#!/usr/bin/python
#coding:utf-8
import time
import re
from subprocess import Popen, PIPE
import os
import SQLTool
import config,portscantask
from nmaptoolbackground.control import taskcontrol
from nmaptoolbackground.model import job
import Sqldatatask
import Sqldata
import   trace 
import getLocationTool
import sniffertask
portname = {'80':'http','8080':'http','443':'https','22':'telnet','3306':'mysql','873':'rsync'} 
zmapinstance=None
def getObject():
    global zmapinstance
    if zmapinstance is None:
        zmapinstance=Zmaptool()
    return zmapinstance
class Zmaptool:
    def __init__(self):
#         self.sqlTool=SQLTool.getObject()
        self.sqlTool=Sqldatatask.getObject()
        self.config=config.Config
        self.portscan=portscantask.getObject()
        self.getlocationtool=getLocationTool.getObject()
# returnmsg =subprocess.call(["ls", "-l"],shell=True)
    def do_scan(self,port='80',num='10',needdetail='0'):
        path=os.getcwd()
        locate=os.path.split(os.path.realpath(__file__))[0]
#         p= Popen(" ./zmap -B  4M -p "+port+" -N "+num+"   -q -O json", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')
        cmd=" zmap -w "+locate+"/iparea.json  -B  1M -p "+port+" -N "+num+"   -q -O json"
        # p= Popen(" zmap -w /root/github/Scan-T/spidermanage/spidertool/iparea.json -B  1M -p "+port+" -N "+num+"   -q -O json", stdout=PIPE, shell=True)

        import commandtool



#        'sudo zmap -p 80 -B 10M -N 50 -q --output-fields=classification,saddr,daddr,sport,dport,seqnum,acknum,cooldown,repeat  -o - '+
#        '| sudo ./forge-socket -c 50 -d http-req > http-banners.out'

#p= Popen(" ./zmap -B 10M -p 80 -n 100000 ", stdout=PIPE, shell=True,cwd=path+'/zmap-2.1.0/src')

        # p.wait()
        # retcode= p.returncode
        # if retcode==0:
        #     returnmsg=p.stdout.read()
        if True:
            returnmsg=commandtool.command(cmd=cmd)
            p = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
            list= p.findall(returnmsg)
#             self.sqlTool.connectdb()
            localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
            insertdata=[]
            jobs=[]
            for i in list:
                insertdata.append((str(i),port,localtime,'open',str(port)))
                self.getlocationtool.add_work([str(i)])

                if needdetail=='0':
                    global portname
                    nowportname=portname.get(port,'')
                    self.portscan.add_work([(nowportname,str(i),port,'open','','')])
                else:
                    
                    ajob=job.Job(jobaddress=str(i),jobport='',forcesearch='0',isjob='0')
                    jobs.append(ajob)
            if needdetail!='0':
                tasktotally=sniffertask.getObject()

                tasktotally.add_work(jobs)
            extra=' on duplicate key update  state=\'open\' , timesearch=\''+localtime+'\''
            
            
#             self.sqlTool.inserttableinfo_byparams(table=self.config.porttable,select_params=['ip','port','timesearch','state'],insert_values=insertdata,extra=extra)
            sqldatawprk=[]
            dic={"table":self.config.porttable,"select_params":['ip','port','timesearch','state','portnumber'],"insert_values":insertdata,"extra":extra}
            tempwprk=Sqldata.SqlData('inserttableinfo_byparams',dic)
            sqldatawprk.append(tempwprk)
            self.sqlTool.add_work(sqldatawprk)
        # try:
        #
        #     p.terminate()
        #
        # except Exception,e:
        #     print e
        #     print 'error'

#             self.sqlTool.closedb()


if __name__ == "__main__":
    temp=Zmaptool()
    temp.do_scan()
    












 
