#!/usr/bin/python
#coding:utf-8
#!/usr/bin/python
#coding:utf-8
from spidertool.ThreadTool import ThreadTool
import datetime
import time
from lib.logger import initLog
from spidertool import config,webconfig
from spidertool.TaskTool import TaskTool
import objgraph
import gc
from plugins import default 

pocscantaskinstance=None
def getObject():
    global pocscantaskinstance
    if pocscantaskinstance is None:
        pocscantaskinstance=PocsearchTask(1)
    return pocscantaskinstance
class PocsearchTask(TaskTool):
    def __init__(self,isThread=1,deamon=False):
        TaskTool.__init__(self,isThread,deamon=deamon)
        logger = initLog('POCDect.log', 3, True)
        self.pocscan=default.PocController(logger=logger)
        self.set_deal_num(1)



    def task(self,req,threadname):
        print threadname+'POC检测任务启动'+str(datetime.datetime.now())
        
        head='' if req[0] is None else req[0]
        context='' if req[1] is None else req[1]
        ip='' if req[2] is None else req[2]
        port='' if req[3] is None else req[3]
        productname='' if req[4] is None else req[4]
        keywords='' if req[5] is None else req[5]
        nmapscript='' if req[6] is None else req[6]
        protocol='' if req[7] is None else req[7]
#         print 'poc   未启动内存增长状况'
#         gc.collect()
#         objgraph.show_growth()
#         temp=default.PocController(logger=logger)
        self.pocscan.detect(head=head, context=context, ip=ip, port=port, productname=productname, keywords=keywords, hackinfo=nmapscript)

#         self.pocscan.detect(head=head, context=context, ip=ip, port=port, productname=productname, keywords=keywords, hackinfo=nmapscript)
        
        print threadname+'POC检测任务结束'+str(datetime.datetime.now())
#         print 'poc   内存增长状况'
#         gc.collect()
#         objgraph.show_growth()
#         print 'objgraph.by_type:',objgraph.by_type('dict')
#         chain =objgraph.find_backref_chain(objgraph.by_type('dict')[-1],inspect.ismodule)
#         objgraph.show_chain(chain,filename='chain.png')
        ans=''
        
        return ans

if __name__ == "__main__":

    pass




