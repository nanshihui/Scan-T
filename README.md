# toolforspider

[![Build Status](http://nanshihui.github.io/public/build)](http://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) [![Python 2.6|2.7](http://nanshihui.github.io/public/python)](https://www.python.org/) [![License](http://nanshihui.github.io/public/license)](http://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) 

toolforsipder is an open source penetration testing tool that automates the process of detecting and collecting the hosts flaws and port fingerprinting. It comes with a powerful detection engine, many niche features for the ultimate penetration tester .

Screenshots
----

![Screenshot](http://nanshihui.github.io/public/result.png)

* Simple introduction:[Screenshot Preview](http://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/)

Installation
----

you can download toolforspider by cloning the [Git](https://github.com/nanshihui/toolforspider) repository:

    git clone https://github.com/nanshihui/toolforspider.git

toolforspider works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on any platform.

Usage
----

To get a list of basic options and switches use:

    sudo python manage.py runserver localhost:80


    
##spidertool 爬虫相关工具包
* src    爬虫独立逻辑代码后期的更新都放到spidermanage里面的sipdertool的文件夹了(spider  code,the new one is in the document which named sipdertool from spidermanage)
* spidermanage     爬虫后台管理类(a web manage about the spider to control the task )

### 注意事项
* spidermanage里面已经包含src里面的相关文件,独立保留一份，方便移植,后期将删除，最新版本的独立文件在spidermanage里面的sipdertool的文件夹了

### 后台主程序在spidermanage文件夹下的manage.py

* PS:if want to help with me to complete this project ...please fork it ^_^

