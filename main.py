#!/usr/bin/python
#coding:utf-8
import urllib
import urllib2
import cookielib
import re
import SQLtool
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
values ={}
#	values['name']='123'
#	values = {'name' : 'Michael Foord', 'location' : 'Northampton', 'language' : 'Python' }

def gethtml(URL,way,params): 
	"""
	启用代理模块
	"""
	enable_proxy=False
	proxy_handler= urllib2.ProxyHandler({"http":'http://someproxy.com:80'})
	null_proxy_handler= urllib2.ProxyHandler({})

	url = URL
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

	headers = { 'User-Agent' : user_agent,
	    'Referer':'http://www.cnbeta.com/articles'
	 }
	data = urllib.urlencode(params)
	req=''
	if way=='POST':
		req = urllib2.Request(url, data, headers)
#		req= urllib2.Request(url)
#		req.add_header('User-Agent','Mozilla/4.0')
	elif len(params)==0:
		req= urllib2.Request(url)
		print '执行无参访问'
	else :
		req= urllib2.Request(url+'?'+data)
		print '执行get访问'

	"""
		启动开启调试端口
	"""
	cookie=cookielib.CookieJar()
	httpcookieprocessor=urllib2.HTTPCookieProcessor(cookie)
	httpHandler= urllib2.HTTPHandler(debuglevel=1)
	httpsHandler=urllib2.HTTPSHandler(debuglevel=1)
	opener=''
	if enable_proxy:
		opener=urllib2.build_opener(httpsHandler,httpsHandler,httpcookieprocessor,proxy_handler)
	else:
		opener=urllib2.build_opener(httpsHandler,httpsHandler,httpcookieprocessor,null_proxy_handler)
	urllib2.install_opener(opener)
	try:

		#response = urllib2.urlopen(req)
		response = urllib2.urlopen('http://www.baidu.com',timeout=10)
		print 'cooke信息如下：'
		for item in cookie:
			print 'Name = '+item.name
			print 'Value = '+item.value
	except urllib2.HTTPError,e:
		print e.code

	the_page = response.read()
	return the_page
html=gethtml('http://drops.wooyun.org/','GET',{})

def dealhtml(html):
	print ''
	


def getImg(html):
    	reg = r'src="(.+?\.jpg)" pic_ext'
    	imgre = re.compile(reg)
    	imglist = re.findall(imgre,html)
    	return imglist  

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

