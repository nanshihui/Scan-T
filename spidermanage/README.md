# toolforspider
###state:coding
a new spider with more function
##spidermanage 爬虫后台相关工具包
* route                         					根据路径初步分配url(decide the url py path)
* view                            				资源文件夹存放前端文件(a place for html and grapic )
* spidermanage         					web端配置文件模块(config of django)
* nmaptoolbackground 			/nmaptool子路径下的具体细分处理(the specific ways to deal with the path)
* zmap 为开源工具
* fontsearch         					用户搜索模块整体，里面是一个独立的web项目。拆开模块写是为了方便移植
* common_static         			存储静态文件。
* sqldata         					数据库文件

##TODO
* 添加nmap扫描跟随zmap
* 查看是否存在内存泄露
* 优化任务调度
* 添加漏洞库