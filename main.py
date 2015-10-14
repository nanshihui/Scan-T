#!/usr/bin/python
import urllib
import re
import SQLtool
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
#people.closedb()
#people.inserdata()
