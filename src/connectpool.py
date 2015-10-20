#!/usr/bin/python
#coding:utf-8

import connecttool
from Queue import Queue
class ConnectPool:
		self.__connect_pool = Queue(maxsize=10) 		#连接池
	def  getConnect(self,URL,way='GET',params={},times=1):
		
		if (self.__connect_pool.full()==False)
		page=self.getHTML(self,URL,way='GET',params={},times=1)
		return page