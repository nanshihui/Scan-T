#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
class TaskTool:
	def __init__(self,isThread=1,deamon=True,needfinishqueue=0):
		self.threadtool=ThreadTool(isThread,deamon=deamon,needfinishqueue=needfinishqueue)
		self.threadtool.add_task(self.task)

	def set_deal_num(self,num):
		self.threadtool.set_Thread_size(num)
	###
	#	添加作业的时候，是添加一个数组进去的，避免频繁的添加
	#
	#
	###
	def add_work(self,work):
		self.threadtool.push(work)

	def task(self,req,threadname):
		print threadname+'执行任务中'+str(datetime.datetime.now())
		ans =threadname+'任务结束'+str(datetime.datetime.now()) 
		return ans
	def start_task(self):
		self.threadtool.start()
	def get_finish_work(self):
		if self.threadtool.taskleft()>0:

			return self.threadtool.pop()
		else:
			return 
	def has_work_left(self):
		return self.threadtool.taskleft()
