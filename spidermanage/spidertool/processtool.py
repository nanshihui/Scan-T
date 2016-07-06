# import gevent,multiprocessing
# import multiprocessing.Pool
# class Poc_Base(object):
#     gevent_num = 100            # 协程数
#     process_num = 4             # 进程数
#     count = [0] * process_num   # 每个进程，单独计数
#     progress = 100              # 进度提醒的单位
#
#     def verify(self):
#         pass
#     def verify_count(self):
#         self.count[progress_number] += 1
#         if self.count[progress_number] % progress == 0:
#             save()                                                # 数据存储
#             print "progress %d " % (self.count[progress_number])       # 进度提醒
#         if self.verify():            print "success"
#     # 协程调度函数，分配任务到协程
#     def run_in_gevent(url_list):                    # url_list 每个进程分配到一定量的url
#         pool = Pool(self.gevent_num)
#         for target in url_list:
#             pool.add(gevent.spawn(self.verify_count, url))
#         pool.join()    # 进程调度函数，分配任务到各个进程
#     def run():
#         url_each_process = len(url_list)/process_num
#         for process_number in range(process_num):
#             multiprocessing.Process(target=run_in_gevent, args=(url_list[*:*],)).start()
#         multiprocessing.join()
#
# if __name__ == "__main__":
#     # temp=Portscantool()
#     # temp.do_scan(ip='172.20.13.11', port='80')


#!/usr/bin/python
#coding:utf-8

import threading
from threading import Thread,Lock
from Queue import Queue
import time
import random
from threading import stack_size
import datetime
import multiprocessing

import gevent
import gevent.monkey
# gevent.monkey.patch_socket()
stack_size(32768*16)
class ProcessTool:
	def __init__(self,isThread=1,needfinishqueue=0,deamon=True):
		self.isThread=isThread
		self.idletask={}
		self.Threads=[]
		self.alivenum=0
		self.needfinishqueue=needfinishqueue
		self.running = 0
		self.threads_num = 10
		self.deamon=deamon
		self.job=None
		self.default_object=None


		self.lock = multiprocessing.Lock()
		self.q_request=multiprocessing.Queue()
		if self.needfinishqueue>0:
			self.q_finish=multiprocessing.Queue()
		from gevent.queue import JoinableQueue as geventqueue
		from gevent.lock import Semaphore
		self.gevent_request=geventqueue()


	def __del__(self): #解构时需等待两个队列完成
		time.sleep(0.5)



	def getqueue_size(self):
		return self.q_request.qsize()
	def set_Thread_size(self,threads_num=10):
		self.threads_num = threads_num
	def init_add(self,add_init_object):
		self.default_object=add_init_object
	def add_task(self,job):
		self.job=job
#获取当前剩余的任务，用于集群操做
	def get_work(self):
		tmparray=[]
		if self.q_request.qsize()>0:
			try:
				req = self.q_request.get(block=True,timeout=4)
				tmparray.append(req)
				return tmparray
			except:
				return tmparray
		else:
			return tmparray
	def start(self):
		sizenumber=min(self.threads_num,self.q_request.qsize())

		for i in range(sizenumber):
			t = multiprocessing.Process(target=self.getTaskProcess)
			print '进程'+str(i+1)+'  正在启动'
			t.Daemon=self.deamon
			t.start()
			self.Threads.append(t)
			with self.lock:
				self.alivenum+=1

	def get_running_size(self):
		return self.running
	def taskleft(self):
		if self.needfinishqueue>0:
			return self.q_request.qsize()+self.q_finish.qsize()+self.running
		else:
			return self.q_request.qsize()+self.running
	def push(self,req):
		sizenum=len(req)
		for urls in req:
			self.q_request.put(urls)

		threadnownum=0


		with self.lock:
			tempnumb=self.alivenum

		sizenumber = min(self.threads_num - tempnumb, 0)
		if tempnumb<self.threads_num:

			for i in range(sizenumber):
				t = multiprocessing.Process(target=self.getTaskProcess)
				t.Daemon = self.deamon
				t.start()
				self.Threads.append(t)
				with self.lock:
					self.alivenum += 1


	def pop(self):
		return self.q_finish.get()
	def do_job(self,job,req,threadname):
		return job(req,threadname)

	def getTaskProcess(self):
		while True:

			req = self.q_request.get()
			with self.lock:				#要保证该操作的原子性，进入critical area
				self.running=self.running+1

			threadname=multiprocessing.current_process().name

			print '进程'+threadname+'发起请求: '

			ans=self.do_job(self.job,req,threadname)
			if self.needfinishqueue>0:
				self.q_finish.put((req,ans))

			with self.lock:
				self.running= self.running-1
			threadname=multiprocessing.current_process().name

			print '进程'+threadname+'完成请求'





def taskitem(req,threadname):
	print threadname,req,'执行任务中'

	time.sleep(3)
	return threadname,'任务结束'+str(datetime.datetime.now())

#TODO 启用一个变量直接判断当前线程数量，而不是每次手动的去判断，减少时间,判断活着的数量在第一次时不要清除线程相关操作
if __name__ == "__main__":
	links = [ 'http://www.bunz.edu.com','http://www.baidu.com','http://www.hao123.cx','http://www.cctv.cx','http://www.vip.cx']
	f = ThreadTool(2)
	f.set_Thread_size(3)
	f.add_task(taskitem)
	# f.start()
# 	for url in links:
#
# 		f.push(url)
	f.push(links)
	f.push(links)

	f.push(links)
	f.push(links)
	f.push(links)
	f.push(links)

# 	f.start()
	timea=1

	time.sleep(20)
	f.push(links)
	f.push(links)
	f.push(links)

	f.push(links)
	# while True:
	# 	pass

