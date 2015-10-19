#!/usr/bin/python
#coding:utf-8
import urllib2
from threading import Thread,Lock
from Queue import Queue
import time
import connecttool
from threading import stack_size
stack_size(32768*16)
class Threadtool:
    	def __init__(self,threads_num):

        		self.lock = Lock() #线程锁
        		self.q_request = Queue() #任务队列
        		self.q_finish = Queue() #完成队列
        		self.threads_num = threads_num

        		self.running = 0
 
    	def __del__(self): #解构时需等待两个队列完成
        		time.sleep(0.5)
        		self.q_request.join()
        		self.q_finish.join()
 	def start(self):
 		for i in range(self.threads_num):
            			t = Thread(target=self.getTask)
            			print '线程'+str(i)+'  正在启动'
            			t.setDaemon(True)
            			t.start()
    	def taskleft(self):
        		return self.q_request.qsize()+self.q_finish.qsize()+self.running
 
    	def push(self,req):
        		self.q_request.put(req)
 
    	def pop(self):
        		return self.q_finish.get()
 
    	def getTask(self):
            while True:

                 req = self.q_request.get()
                 print req

                 with self.lock:				#要保证该操作的原子性，进入critical area
                         print '123'
                         self.running=self.running+1
#			self.lock.acquire()
#				threadname=threading.currentThread().getName()

#	 			print '进程'+threadname+'发起请求'
                 print '任务执行中'
                 connectTool=connecttool.ConnectTool()
                 ans = connectTool.getHTML(req)

    # 			self.lock.release()
                 self.q_finish.put((req,ans))
#			self.lock.acquire()
                 with self.lock:
                    self.running-= 1
#				threadname=threading.currentThread().getName()

#	 			print '进程'+threadname+'完成请求'
#			self.lock.release()

                 self.q_request.task_done()

                 time.sleep(0.1) 
if __name__ == "__main__":
    	links = [ 'http://www.bnuz.edu.com','http://www.baidu.com','http://www.youku.com','http://www.tudou.com']
    	f = Threadtool(threads_num=10)
   	for url in links:
		f.push(url)
	f.start()
    	while f.taskleft():
        		url,content = f.pop()
        		print url,(content)