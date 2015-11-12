#!/usr/bin/python
#coding:utf-8
import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_301(self,req,fp,code,msg,headers):
		print '301问题'
	def http_error_302(self,req,fp,code,msg,headers):
		print '302问题'
def formatstring(str):
	return '\''+str+'\''
def setCookies(response,user,time):
	response.set_cookie('islogin',user.islogin,time)
	response.set_cookie('username',user.username,time)
	response.set_cookie('role',user.role,time)
	response.set_cookie('power',user.power,time)
def delCookies(response):
	response.delete_cookie('islogin')
	response.delete_cookie('username')
	response.delete_cookie('role')
	response.delete_cookie('power')
	
	
	