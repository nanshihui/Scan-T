#!/usr/bin/python
#coding:utf-8
import urllib
import urllib2
import cookielib
import re
import SQLtool
import webconfig
import sys 
import webtool
reload(sys)
sys.setdefaultencoding('utf-8')
WEBCONFIG=webconfig.WebConfig
RedirectHandler=webtool.RedirectHandler()
#	values ={}
#	values['name']='123'
#	values = {'name' : 'Michael Foord', 'location' : 'Northampton', 'language' : 'Python' }

def gethtml(URL,way,params): 
	"""
	启用代理模块
	"""
	enable_proxy=WEBCONFIG.enable_proxy
	proxy_handler= urllib2.ProxyHandler({WEBCONFIG.proxy_name:WEBCONFIG.proxy_address})
	null_proxy_handler= urllib2.ProxyHandler({})
#	urllib2.socket.setdefaulttimeout(10)                                    #设置超时时间
	url = URL
	

	headers = { 
		'User-Agent' :	 WEBCONFIG.useragent,
	    	'Referer':	 WEBCONFIG.Referer
	 }
	data = urllib.urlencode(params)
	req=''
	if way=='POST':
		req = urllib2.Request(url, data, headers)
		temp=req.get_full_url()
		print temp
#		req= urllib2.Request(url)
#		req.add_header('User-Agent','Mozilla/4.0')
	elif len(params)==0:
		req= urllib2.Request(url)
		req.add_header('User-Agent',WEBCONFIG.useragent)
		req.add_header('Referer',WEBCONFIG.Referer)
		print '执行无参访问'
	else :
		req= urllib2.Request(url+'?'+data)
		print '执行get访问'
		print url+'?'+data


	"""
		启动开启调试端口
	"""
	cookie=cookielib.CookieJar()
	cJar=cookielib.LWPCookieJar()
	httpcookieprocessor=urllib2.HTTPCookieProcessor(cookie)
	httpHandler= urllib2.HTTPHandler(debuglevel=1)
	httpsHandler=urllib2.HTTPSHandler(debuglevel=1)
	opener=''
	if enable_proxy:
		opener=urllib2.build_opener(httpcookieprocessor,proxy_handler,httpsHandler,httpsHandler,RedirectHandler)
	else:
		opener=urllib2.build_opener(httpcookieprocessor,null_proxy_handler,httpsHandler,httpsHandler,RedirectHandler)
	urllib2.install_opener(opener)
	opener.handle_open['http'][0].set_http_debuglevel(1) 
	#获得详细发送请求信息
	try:

		response = urllib2.urlopen(req)


#		response = urllib2.urlopen('http://www.baidu.com',timeout=10)
		print 'head is %s' % response.info()
		print 'cooke信息如下：'
		for item in cookie:
			print 'Name = '+item.name
			print 'Value = '+item.value
		the_page = response.read()
		response.close()
		return the_page
	except urllib2.HTTPError,e:
		print '错误码为: %s' % e.code

		#response.close()
		return 

def geteasyconnet():
	httpHandler =urllib2.HTTPHandler(debuglevel=1)
	httpsHandler =urllib2.HTTPSHandler(debuglevel=1)
	opener =urllib2.build_opener(httpHandler, httpsHandler) 
	urllib2.install_opener(opener)
	response = urllib2.urlopen('http://www.baidu.com')
#geteasyconnet()

def dealhtml(html):
	print html
	


def getImg(html):
    	reg = r'src="(.+?\.jpg)" pic_ext'
    	imgre = re.compile(reg)
    	imglist = re.findall(imgre,html)
    	return imglist  

html=gethtml('http://drops.wooyun.org','GET',{})
dealhtml(html)
#html = getHtml("http://www.baidu.com")

#print getImg(html)
#while true:
#	interpert()
#	print 'please input the item you want: ',



#people=SQLtool.DBmanager()
#people.connectdb()
#people.searchtableinfo_byparams(['book'],[],['author'],['\'王珊\''])
#people.showdata()
#people.showtableinfo('book',['bid','title','author','press','price'])
#people.searchtableinfo('book','bid','1001')
#people.searchtableinfo_byitem(['users','orders'],['oid','user','name','ordertime','orders.state','payment'],['uid','user'],'102')
#people.searchtableinfo_byitemmore(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime'],['','bookid'],'1001')
#people.searchtableinfo_byitemmore(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime'],['','title'],'经济学原理')

#people.searchtableinfo_bystate(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime','orders.state'],['','bookid'],('1001',4))
#people.searchtableinfo_bystate(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime','orders.state'],['',],(4))
#people.inserdata()
#people.closedb()

