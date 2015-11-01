#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import connectpool
from TaskTool import TaskTool
import SQLTool
import HTMLParser

    
class dealTask(TaskTool,HTMLParser.HTMLParser):
    ##处理任务类，通过将爬虫爬回来的网页信息进行进一步的处理
    def __init__(self):
        TaskTool.__init__(self)
        HTMLParser.HTMLParser.__init__(self)
        self.connectpool=connectpool.ConnectPool()

    def task(self,req,threadname):
        print threadname+'执行任务中'+str(datetime.datetime.now())
        ans = self.makesqlit(req[1])


        print threadname+'任务结束'+str(datetime.datetime.now())
        return ans
                                                                                                    #该方法用来处理开始标签的，eg:<div id="main">  
    def handle_starttag(self, tag, attrs):  
        if tag == 'a':                                                                          #如果为<a>标签  
                                                                                                    #name为标签的属性名，如href、name、id、onClick等等  

            for name,value in attrs:      
                if name == 'href':                                                     #这时选择href属性  
                    print "name_value: ",value                              #href属性的值  
                    print "first tag:",self.get_starttag_text()     #<a>标签的开始tag  
                    print "\n"
    def makesqlit(self,content):
        self.feed(content.decode('UTF-8'))
        self.close()
#        return content
if __name__ == "__main__":
    """
    DealSQL=SQLTool.DBmanager()
    DealSQL.connectdb()
    (result,title,count,col)=DealSQL.searchtableinfo_byparams(['webdata'],['address','content','meettime'])
    DealSQL.closedb()
    #TODO 添加元组进去
    #ｕｒｌ也要存进去
    f = dealTask()
    f.set_deal_num(10)


    for data in result:
        f.add_work([(data[0],data[1])])
#        print data[1]

    f.start_task()
    while f.has_work_left():
        v,ans=f.get_finish_work()
        print ans
    while True:
        pass

    """

    try:
        file_object = open('test.html')
        content = file_object.read( )
        file_object.close( )
    except Exception,e:
        print e
    TOOL=dealTask()
    TOOL.makesqlit(content)




