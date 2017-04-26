#!/bin/bash
#####haven't finished yet. Do not use it!!!!
help="haven't finished yet. Do not use it!!!!"
echo $help
username="root"
password="123456"

apt-get install -y nmap
apt-get install -y libjson-c-dev libjson-c2  libjson0 libjson0-dev
apt-get install -y redis-server zmap libffi-dev libssl-dev python-pip libmysqlclient-dev
apt-get install -y wget unzip

apt-get install mysql-server
apt-get install mysql-client
apt-get install libmysqlclient-dev

apt-get -y install python-dev


apt-get install python-mysqldb
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple BeautifulSoup==3.2.1
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4==4.4.1
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple Django==1.9
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple python-nmap==0.5.0
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple DBUtils==1.1
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple paramiko==1.16.0
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple ruamel.ordereddict==0.4.9
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple scapy==2.3.3
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple scapy-http==1.7
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple objgraph==2.0.1
pip install   -i https://pypi.tuna.tsinghua.edu.cn/simple pycrypto==2.6.1
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple dozer
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple faulthandler
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple apscheduler
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple gevent
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple redis
pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple chardet




# ####download SO file
# wget https://nanshihui.github.io/public/mysqlcft.so
# mysqlcftpath=$(pwd)'/mysqlcft.so'
# #mysqldestfile=
# command_sql='show processlist;'
# mysql_plugin_file='/usr/lib/mysql/plugin/mysqlcft.so'



# service mysql start

# ####cp SO file to mysql plugin root path 
# result=$(cp $mysqlcftpath $mysql_plugin_file)






#echo $result
# initpluginsql='Install plugin mysqlcft soname "mysqlcft.so"'






# ####init SO file
# result=$(mysql -u${username} -p${password}  -s -e "${initpluginsql}")
#create database
create_sql="create database datap;"
result=$(mysql -u${username} -p${password}  -s -e "${create_sql}")



####init database
init_sql="source $(pwd)/../spidermanage/sqldata/Dump20160803.sql"
result=$(mysql -u${username} -p${password} -Ddatap -s -e "${init_sql}")



####add user to database
adduser='insert into user_table values("admin",3,3,"admin")'
result=$(mysql -u${username} -p${password} -Ddatap -s -e "${adduser}")


$(cd ../spidermanage&&mkdir logs)



