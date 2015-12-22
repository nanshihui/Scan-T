#!/usr/bin/python
#coding:utf-8

import connecttool
import Queue
import gc
connectpoolinstance=None
def getObject():
	global connectpoolinstance
	if connectpoolinstance is None:
		connectpoolinstance=ConnectPool()
	return connectpoolinstance
class ConnectPool:

	def __init__(self,poolsize=10):
		self.__connect_pool = Queue.Queue(maxsize=poolsize) 		#连接池
		self.connectTool=connecttool.ConnectTool()
#		self.__connect_pool.put(connectTool,block=False)
	def check_network(self):
		import httplib2 
		try: 
			http = httplib2.Http() 
			resp, content = http.request("http://www.baidu.com") 
		except: 
				return 0
		return 1 
	def  getConnect(self,URL,way='GET',params={},times=1):
		self.__connect_pool.put(1)
		print '当前访问的位置为： '+URL
# 		gc.enable() 
# 		gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK|gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)
		head,page=self.connectTool.getHTML(URL,way,params,times)
# 		po=gc.collect()
# 		print po
		self.__connect_pool.get()
		self.__connect_pool.task_done()
		return head,page
"""
		try:

			self.__connect_pool.put()

		except Queue.Empty:
			connectTool=connecttool.ConnectTool()


		finally:
			page=connectTool.getHTML(self,URL,way='GET',params={},times=1)


		try :
			self.__connect_pool.put(connectTool,block=False)
		except Queue.Full:
			pass
		return page
"""
