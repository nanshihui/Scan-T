# Scan-T

[![Build Status](https://nanshihui.github.io/public/status.svg)](https://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) [![Python 2.7](https://nanshihui.github.io/public/python.svg)](https://www.python.org/) [![License](https://nanshihui.github.io/public/license.svg)](https://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) 

　　Scan-T is an open source penetration testing tool that automates the process of detecting and collecting the hosts flaws and port fingerprinting. It comes with a powerful detection engine, many nice features for the ultimate penetration tester .

Project Framework
----
　　nginx,django,uwsgi

Search Framework
----
　　elasticsearch,redis

Screenshots
----
* searching struts vulnerability 

![Screenshot](https://nanshihui.github.io/public/struts.png)

</br>

* struts vulnerability distribution

![Screenshot](https://nanshihui.github.io/public/locate.png)

</br>

* the location of computer

![Screenshot](https://nanshihui.github.io/public/mapshow.png)


* Simple introduction:[Screenshot Preview](https://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/)

Require
----
* Zmap
* Nmap

Installation
----

you can download Scan-T by cloning the [Git](https://github.com/nanshihui/Scan-T) repository:

    git clone https://github.com/nanshihui/Scan-T.git
    
Install introduction: [here](https://github.com/nanshihui/Scan-T/wiki/Install-introduction)

Scan-T works out of the box with [Python](http://www.python.org/download/) version  **2.7.x** on any platform.

Usage
----

To get a list of basic options and switches use:

    sudo python spidermanage/manage.py runserver localhost:80 --insecure
    
Notice
----
* spidermanage     
a network management platform about the spider to control the task 
* PS:if want to help with me to complete this project ...please fork it ^_^  
* Commercial uses are strictly prohibited.





