#!/usr/bin/python
#coding:utf-8
import urllib
import re
import SQLtool
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
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

def interpert():
	print''' welcome to use '''
	print''' 1.search book by id  '''
	print''' 2.search book by name  '''
	print''' 3.search book by   '''
	print''' '''
interpert()
people=SQLtool.DBmanager()
people.connectdb()
#people.showdata()
people.showtableinfo('book',['bid','title','author','press','price'])
#people.searchtableinfo('book','bid','1001')
#people.searchtableinfo_byitem(['users','orders'],['oid','user','name','ordertime','orders.state','payment'],['uid','user'],'102')
#people.searchtableinfo_byitemmore(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime'],['','bookid'],'1001')
#people.searchtableinfo_byitemmore(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime'],['','title'],'经济学原理')

#people.searchtableinfo_bystate(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime','orders.state'],['','bookid'],('1001',4))
#people.searchtableinfo_bystate(['users','book','orders','orderbook'],['orderid','bookid','title','author','press','quantity','user','name','ordertime','orders.state'],['',],(4))
#people.inserdata()
people.closedb()

