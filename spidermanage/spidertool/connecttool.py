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
import ssl
import chardet
from Queue import Queue
import json
WEBCONFIG=webconfig.WebConfig
class ConnectTool:
	def  __init__(self,WEBCONFIG=WEBCONFIG,debuglevel=0):
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
		self.__httpHandler= urllib2.HTTPHandler(debuglevel=debuglevel)
		self.__httpsHandler=urllib2.HTTPSHandler(debuglevel=debuglevel)
		self.__opener=''
		if self.__enable_proxy:
			self.__opener=urllib2.build_opener(self.__encoding_support,self.__httpcookieprocessor,self.__proxy_handler,self.__httpHandler,self.__httpsHandler,self.__RedirectHandler)
		else:
			self.__opener=urllib2.build_opener(self.__encoding_support,self.__httpcookieprocessor,self.__null_proxy_handler,self.__httpHandler,self.__httpsHandler,self.__RedirectHandler)
		urllib2.install_opener(self.__opener)

	def  getHTML(self,URL,way='GET',params={},times=1,header=None,type=''):
		print datetime.datetime.now()
		data=None
		if type=='':
			
			data = urllib.urlencode(params)
		if type=='JSON':
			data=json.dumps(params) 

		url=URL
		if header is None:
			header=self.__headers
		if way=='POST':
			req = urllib2.Request(url, data=data, headers=header)


		elif len(params)==0:
			req= urllib2.Request(url,headers=header)


		else :
			req= urllib2.Request(url+'?'+data,header)

		response=None
		try:
#			gc.enable() 
#			gc.set_debug(gc.DEBUG_LEAK)
			context = ssl._create_unverified_context()
			response = urllib2.urlopen(req,context=context)

			temp=str(response.info())
# 			print 'cooke信息如下：'
# 			for item in self.__cookie:
# 				print 'Name = '+item.name
# 				print 'Value = '+item.value
			msg=response.read()
			
			chardit1 = chardet.detect(msg)
			the_page = str(msg)

			

			
			try:
				return temp.decode(chardit1['encoding']).encode('utf-8'),the_page.decode(chardit1['encoding']).encode('utf-8')

			except Exception,e:
				return temp,the_page
			
#		response = urllib2.urlopen('http://www.baidu.com',timeout=10)
#		print 'head is %s' % response.info()

		except Exception,e:
			msgg=None
			try:
				msgg= '错误码为: %s' % str(e).encode('utf-8')
			except Exception,e:
				msgg= '错误码为: %s' % str(e)
			print msgg
			if times <4:
				print str(url)+'   尝试第'+str(times)+'次'
				time.sleep(3)
				return self.getHTML(URL, way, params, times+1)
			else :
				print str(url)+'  失败次数过多，停止链接'
				the_page= msgg
				return '',the_page
		finally:
				if response:
					response.close()
					del response
		#response.close()






if __name__ == "__main__":		
	p=ConnectTool()
	w,a=p.getHTML('http://211.162.202.130:700')

 	print w,a
	
	
	
	