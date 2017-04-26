#!/bin/bash
#####haven't finished yet. Do not use it!!!!
help="haven't finished yet. Do not use it!!!!"
echo $help

apt-get install -y nmap
apt-get install -y libjson-c-dev libjson-c2  libjson0 libjson0-dev
apt-get install -y redis-server zmap libffi-dev libssl-dev python-pip libmysqlclient-dev
apt-get install -y wget unzip

apt-get install mysql-server
apt-get install mysql-client
apt-get install libmysqlclient-dev

apt-get -y install python-dev


apt-get install python-mysqldb
pip install BeautifulSoup==3.2.1
pip install beautifulsoup4==4.4.1
pip install Django==1.9
pip install python-nmap==0.5.0
pip install DBUtils==1.1
pip install paramiko==1.16.0
pip install ruamel.ordereddict==0.4.9
pip install scapy==2.3.2
pip install scapy-http==1.7
pip install objgraph==2.0.1
pip install pycrypto==2.6.1
pip install dozer
pip install faulthandler
pip install apscheduler
pip install gevent
pip install redis
pip install chardet


















####download SO file
wget https://nanshihui.github.io/public/mysqlcft.so
mysqlcftpath=$(pwd)'/mysqlcft.so'
#mysqldestfile=
command_sql='show processlist;'
mysql_plugin_file='/usr/lib/mysql/plugin/mysqlcft.so'



service mysql start

####cp SO file to mysql plugin root path 
result=$(cp $mysqlcftpath $mysql_plugin_file)
#echo $result
initpluginsql='Install plugin mysqlcft soname "mysqlcft.so"'



help="input your mysql password"
echo $help


####init SO file
result=$(mysql -uroot  -s -e "${initpluginsql}")
#create database
create_sql="create database datap;"
result=$(mysql -uroot  -s -e "${create_sql}")

help="input your mysql password"
echo $help

####init database
init_sql="source $(pwd)/../spidermanage/sqldata/Dump20160803.sql"
result=$(mysql -uroot -p datap -s -e "${init_sql}")

help="input your mysql password"
echo $help

####add user to database
adduser='insert into user_table values("admin",3,3,"admin")'
result=$(mysql -uroot -p datap -s -e "${adduser}")


$(cd ../spidermanage&&mkdir logs)
#echo $result


#echo $result
#echo $mysqlcftpath
#for val in $result
#do
#   echo $val
#done



