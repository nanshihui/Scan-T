#!/usr/bin/python
#coding:utf-8
import urllib
import urllib2
import cookielib
import webconfig
import sys 
import webtool
import gzipsupport
import time
import datetime
import gc
from Queue import Queue
WEBCONFIG=webconfig.WebConfig
class ConnectTool:
	def  __init__(self,WEBCONFIG=WEBCONFIG,debuglevel=1):
		self.__RedirectHandler=webtool.RedirectHandler()
		self.__encoding_support = gzipsupport.ContentEncodingProcessor()
		"""
		启用代理模块
		"""
		self.__enable_proxy=WEBCONFIG.enable_proxy
		self.__proxy_handler= urllib2.ProxyHandler({WEBCONFIG.proxy_name:WEBCONFIG.proxy_address})
		self.__null_proxy_handler= urllib2.ProxyHandler({})
		urllib2.socket.setdefaulttimeout(WEBCONFIG.time_out)                                    #设置超时时间
		self.__headers = { 
			'User-Agent' :		 WEBCONFIG.useragent,
	    		'Referer':		 WEBCONFIG.Referer
			 }

		self.__cookie=cookielib.CookieJar()
		self.__cJar=cookielib.LWPCookieJar()
		self.__httpcookieprocessor=urllib2.HTTPCookieProcessor(self.__cookie)
		self.__httpHandler= urllib2.HTTPHandler(debuglevel=1)
		self.__httpsHandler=urllib2.HTTPSHandler(debuglevel=1)
		self.__opener=''
		if self.__enable_proxy:
			self.__opener=urllib2.build_opener(self.__encoding_support,self.__httpcookieprocessor,self.__proxy_handler,self.__httpHandler,self.__httpsHandler,self.__RedirectHandler)
		else:
			self.__opener=urllib2.build_opener(self.__encoding_support,self.__httpcookieprocessor,self.__null_proxy_handler,self.__httpHandler,self.__httpsHandler,self.__RedirectHandler)
		urllib2.install_opener(self.__opener)

	def  getHTML(self,URL,way='GET',params={},times=1):
		print datetime.datetime.now()
		data = urllib.urlencode(params)

		url=URL
		req=''
		if way=='POST':
			req = urllib2.Request(url, data=data, headers=self.__headers)

#			req= urllib2.Request(url)
#			req.add_header('User-Agent','Mozilla/4.0')
		elif len(params)==0:
			req= urllib2.Request(url,headers=self.__headers)
			print '执行get访问'
#			req.add_header('User-Agent',WEBCONFIG.useragent)
#			req.add_header('Referer',WEBCONFIG.Referer)
#			print '执行无参访问'
		else :
			req= urllib2.Request(url+'?'+data,headers=self.__headers)
			print '执行get访问'
		
		try:
#			gc.enable() 
#			gc.set_debug(gc.DEBUG_LEAK)
			response = urllib2.urlopen(req)

			print 'cooke信息如下：'
			for item in self.__cookie:
				print 'Name = '+item.name
				print 'Value = '+item.value
			the_page = response.read()

			response.close()

			del response


#			gc.collect()

			return the_page
#		response = urllib2.urlopen('http://www.baidu.com',timeout=10)
#		print 'head is %s' % response.info()

		except Exception,e:

			print '错误码为: %s' % e
			if times <4:
				print '尝试第'+str(times)+'次'
				time.sleep(3)
				return self.getHTML(URL, way, params, times+1)
			else :
				print '失败次数过多，停止链接'
				the_page= ' 失败的连接'
				return the_page
		#response.close()






if __name__ == "__main__":		
	p=ConnectTool()
	w=p.getHTML('http://www.bnuz.edu.com')
	print 'result is ：   '+w