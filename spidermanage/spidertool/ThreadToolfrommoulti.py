#!/usr/bin/python
#coding:utf-8
import urllib2
import threading
from threading import Thread,Lock
import Queue
import time
import connectpool
from threading import stack_size
import datetime
import multiprocess
import multiprocessing

class Threadbase(threading.Thread):
	def __init__(self, work_queue):

		threading.Thread.__init__(self)
		self.work_queue = work_queue
		self.start()

	def run(self):
#死循环，从而让创建的线程在一定条件下关闭退出
		while True:
			try:
				do, args = self.work_queue.get(block=False)#任务异步出队，Queue内部实现了同步机制
				do(args)
				self.work_queue.task_done()#通知系统任务完成
			except:
				threadname=threading.currentThread().getName()
				print '没有任务检测到,关闭多余资源'+threadname
				break
class Processbase(multiprocess.Process):
	def __init__(self, work_queue):
		multiprocess.Process.__init__(self)
		self.work_queue = work_queue
		self.start()

	def run(self):
#死循环，从而让创建的线程在一定条件下关闭退出
		while True:
			try:
				threadname=multiprocess.current_process().name
				print '正在执行任务'+threadname
				do,args = self.work_queue.get(block=False)#任务异步出队，Queue内部实现了同步机制
				print '正在读取数据'+threadname
				do(args)
				print '结束当前操作'+threadname
			except:
				threadname=multiprocess.current_process().name
				print '没有任务检测到,关闭多余资源'+threadname
				break	

stack_size(32768*16)

class ThreadTool:
	def __init__(self,isThread=1):
		self.isThread=isThread
		self.Threads=[]
		self.idletask={}
		self.threads_num=None
		self.work_num=None
		self.default_object=None
		self.job=None
#		self.running = 0

#	def __del__(self): #解构时需等待两个队列完成
#		time.sleep(0.5)
#		if self.isThread==1:

#			self.q_request.join()
#			self.q_finish.join()
		if self.isThread==1:
#			self.lock = Lock() #线程锁
			self.work_queue = Queue.Queue()#任务队列
			self.lock = Lock() #线程锁
#			self.q_request = Queue() #任务所处理的对象队列
#			self.q_finish = Queue() #任务所处理的对象完成队列
		else :
#			self.lock = multiprocessing.Lock()  
#			self.q_request=multiprocessing.Queue()
#			self.q_finish=multiprocessing.Queue()
			self.lock = multiprocessing.Manager().Lock()  
			temp=multiprocess.Manager()
			self.work_queue = temp.Queue()#任务队列


	def set_Thread_size(self,threads_num=10):
		self.threads_num = threads_num#设置总线程数或总进程数
	def set_Work_size(self,work_num=1):#设置总任务数量
		self.work_num = work_num
	def append_Work(self,jobdeal,jobgave):
		if len(jobdeal)==len(jobgave):
			threadnownum=0
			threaddie=[]
			dienum=0
			if self.isThread==1:
				for item in self.Threads:

					if item.isAlive():

						threaddie.append(dienum)
						threadnownum=threadnownum+1
					dienum=dienum+1

				with self.lock:	
					print str(threadnownum)+'活着的线程数'
					self.Threads = filter(lambda x:x.isAlive() !=False,self.Threads)
			else:
				for item in self.Threads:

					if item.is_alive():
						threaddie.append(dienum)
						threadnownum=threadnownum+1	
					dienum=dienum+1

				with self.lock:	
					print str(threadnownum)+'活着的进程数'
					self.Threads = filter(lambda x:x.is_alive()!=False,self.Threads)
			print str(len(self.Threads))+'清理后活着的进程数'


			
			sizenumber=min(self.threads_num-threadnownum,len(jobdeal))
			self.add_Work(jobdeal,jobgave)
			if self.isThread==1:
				for i in range(sizenumber):
					t=Threadbase(self.work_queue)
					t.Daemon=True
					self.Threads.append(t)

			else:
				for i in range(sizenumber):
					t=Processbase(self.work_queue)
					t.Daemon=True
					self.Threads.append(t)

		else:
			print 'no work arrange'
			return	
	def add_Work(self,jobdeal,jobgave):
		if len(jobdeal)==len(jobgave):
			for i in range(len(jobdeal)):
#				self.__add_each_work(self.do_job,jobgave[i])
#				_bound_instance_method_alias = functools.partial(_instance_method_alias, self)
#				self.__add_each_work(_bound_instance_method_alias,i)
				self.__add_each_work(jobdeal[i],jobgave[i])
		else:
			print 'no work arrange'
			return	
	def __add_each_work(self, func,args):

		try:

			self.work_queue.put((func,args))#任务入队，Queue内部实现了同步机制
		except BaseException,e:
			print e
			
	def init_add(self,add_init_object):
		self.default_object=add_init_object
	def add_task(self,job):
		self.job=job

	def start(self):
		sizenumber=min(self.threads_num,self.work_queue.qsize())
		print str(sizenumber)+'   当前启动数量为'
		if self.isThread==1:

			for i in range(sizenumber):
				t=Threadbase(self.work_queue)
				t.Daemon=True
				self.Threads.append(t)
#				t = Thread(target=self.getTask)
#				print '线程'+str(i+1)+'  正在启动'
#
#				t.start()
		else:
			for i in range(sizenumber):

				temp=Processbase(self.work_queue)
				temp.Daemon=True
				self.Threads.append(temp)
#				t = multiprocessing.Process(target=self.getTaskProcess)
#				print '进程'+str(i+1)+'  正在启动'
#				t.Daemon=True
#				t.start()	
#	
#	def taskleft(self):
#		return self.q_request.qsize()+self.q_finish.qsize()+self.running
#

####TODO 增加插入任务，如何线程未达到最大值，继续创建新线程

#	def push(self,req):
#		self.q_request.put(req)

#	def pop(self):
#		return self.q_finish.get()
#	def do_job(self,job,req,threadname):
#		return job(req,threadname)

#	def getTaskProcess(self):
#		while True:
#			if self.taskleft()>0:
#				try:
#					req = self.q_request.get(block=True,timeout=5)
#				except:
#					continue
#			else:
#				threadname=multiprocessing.current_process().name
#				print threadname+'关闭'
#				break
#			with self.lock:				#要保证该操作的原子性，进入critical area
#				self.running=self.running+1

#			threadname=multiprocessing.current_process().name

#			print '进程'+threadname+'发起请求: '

#			ans=self.do_job(self.job,req,threadname)



#			self.q_finish.put((req,ans))

#			with self.lock:
#				self.running-= 1
#			threadname=multiprocessing.current_process().name

#	 		print '进程'+threadname+'完成请求'




#	def getTask(self):
#		while True:
#			if self.taskleft()>0:
#				try:
#					req = self.q_request.get(block=True,timeout=5)
#				except:
#					continue
#			else:
#				threadname=threading.currentThread().getName()
#				print threadname+'关闭'
#				break
#			with self.lock:				#要保证该操作的原子性，进入critical area
#				self.running=self.running+1

#			threadname=threading.currentThread().getName()

#			print '线程'+threadname+'发起请求: '

#			ans=self.do_job(self.job,req,threadname)



#			self.q_finish.put((req,ans))

#			with self.lock:
#				self.running-= 1
#			threadname=threading.currentThread().getName()

#	 		print '线程'+threadname+'完成请求'


#			self.q_request.task_done()

	def wait_allcomplete(self):
		if self.isThread==1:
			for item in self.Threads:
				if item.isAlive():
					item.join()
		else:
			for item in self.Threads:
				if item.is_alive():
					item.join()	
	#具体要做的任务
	def do_job(self,args):

		if self.isThread==1:
			print threading.current_thread(),args
		else:
			print datetime.datetime.now()
			print multiprocess.current_process(),args
def taskitem(req,threadname):
	print threadname+'执行任务中'
	print datetime.datetime.now()
	return threadname+'任务结束'+str(datetime.datetime.now())


if __name__ == "__main__":

#	links = [ 'http://www.bunz.edu.com','http://www.baidu.com','http://www.hao123.cx','http://www.cctv.cx','http://www.vip.cx']
#	f = ThreadTool(0)
#	f.set_Thread_size(10)
#	for url in links:
#		f.push(url)
#	f.add_task(taskitem)
#	f.start()
#	timea=1
#	while f.taskleft():
#		url,content = f.pop()
#		print url
#	while True:
#		pass


	start = time.time()
	work_manager =  ThreadTool(0)#或者work_manager =  WorkManager(10000, 20)
	work_manager.set_Thread_size(1)
	work_manager.set_Work_size(6)
	work_manager.add_Work([work_manager.do_job],['1'])
	#work_manager.add_Work([work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job],['a','b','c','d','e','f','g','h','i','j'])
	work_manager.start()
#	work_manager.append_Work([work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job,work_manager.do_job],['k','l','m','n','o','p','q','r','s','t'])

	work_manager.wait_allcomplete()
	end = time.time()

	print "cost all time: %s" % (end-start)