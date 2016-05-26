# toolforspider

[![Build Status](http://nanshihui.github.io/public/status.svg)](http://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) [![Python 2.6|2.7](http://nanshihui.github.io/public/python.svg)](https://www.python.org/) [![License](http://nanshihui.github.io/public/license.svg)](http://nanshihui.github.io/2016/01/21/ToolForSpider%E7%AE%80%E4%BB%8B/) 

##spidermanage 爬虫后台相关工具包
* route                         					根据路径初步分配url(decide the url py path)
* view                            				资源文件夹存放前端文件(a place for html and grapic )
* spidermanage         					web端配置文件模块(config of django)
* nmaptoolbackground 			/nmaptool子路径下的具体细分处理(the specific ways to deal with the path)
* zmap 为开源工具
* fontsearch         					用户搜索模块整体，里面是一个独立的web项目。拆开模块写是为了方便移植
* common_static         			存储静态文件。
* sqldata         					数据库文件
* spidertool                          					逻辑核心模块
##TODO
* 查看是否还存在内存泄露
* 优化任务调度
* 添加漏洞库