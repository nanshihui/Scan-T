#!/usr/bin/python
#coding:utf-8
import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_301(self,req,fp,code,msg,headers):
		print '301问题'
	def http_error_302(self,req,fp,code,msg,headers):
		print '302问题'
def check_network():
	import httplib2 
	try: 
		http = httplib2.Http() 
		resp, content = http.request("http://www.baidu.com") 
	except: 
		return 0
	return 1 