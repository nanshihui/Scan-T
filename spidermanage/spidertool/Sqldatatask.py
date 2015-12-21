#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import SQLTool
from TaskTool import TaskTool
sqltaskdata=None
def getObject():
	global sqltaskdata
	if sqltaskdata is None:
		sqltaskdata=SqlDataTask()
		sqltaskdata.set_deal_num(1)
	return sqltaskdata
class SqlDataTask(TaskTool):
	def __init__(self,isThread=1):
		TaskTool.__init__(self,isThread)
		self.sqlhelp=SQLTool.getObject()
		self.sqlhelp.connectdb()
	def task(self,req,threadname):
		print threadname+'执行任务中'+str(datetime.datetime.now())
# 		self.sqlhelp.connectdb()
		func=req.getFunc()
		Dic=req.getDic()
		print Dic
		ans=getattr(self.sqlhelp, func,'default')(**Dic)

		
		print threadname+'任务结束'+str(datetime.datetime.now())
# 		self.sqlhelp.closedb()
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




