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
people=SQLtool.DBmanager()
people.connectdb()
#people.showdata()
#people.showtableinfo('book',['bid','title','author','press','price'])
#people.searchtableinfo('book','bid','1001')

people.inserdata()
people.closedb()

