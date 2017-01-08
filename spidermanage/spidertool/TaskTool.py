#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime

class TaskTool:
	def __init__(self,isThread=1,deamon=False,needfinishqueue=0,log=None):
		self.threadtool=ThreadTool(isThread,deamon=deamon,needfinishqueue=needfinishqueue)
		self.threadtool.add_task(self.task)
		self.log=log
		self.threadtool.set_Thread_size(1)
	def set_deal_num(self,num):
		self.threadtool.set_Thread_size(num)
	###
	#	添加作业的时候，是添加一个数组进去的，避免频繁的添加
	#
	#
	###
	def add_work(self,work):
		self.threadtool.push(work)
	def get_work(self):
		return self.threadtool.get_work()
	def task(self,req,threadname):
		print threadname,'执行任务中'+str(datetime.datetime.now())
		print '收到数据：%s' % req
		ans =''
		return ans
	def start_task(self):
		self.threadtool.start()
	def get_finish_work(self):
		if self.threadtool.taskleft()>0:

			return self.threadtool.pop()
		else:
			return None
	def has_work_left(self):
		return self.threadtool.taskleft()
	def get_length(self):
		return self.threadtool.getqueue_size()
	def get_current_task_num(self):
		return self.threadtool.get_running_size()
if __name__=='__main__':
	import time
	t=TaskTool(2)
	t.add_work([1,2,3,4,5])
	t.add_work([6,7,8,9,10])
	t.add_work([16, 17, 18, 19, 110])
