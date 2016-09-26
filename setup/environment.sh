#!/bin/bash
#####haven't finished yet. Do not use it!!!!
help="haven't finished yet. Do not use it!!!!"
echo $help

####download SO file
#wget https://nanshihui.github.io/public/mysqlcft.so
mysqlcftpath=$(pwd)'/mysqlcft.so'
#mysqldestfile=
command_sql='show processlist;'
mysql_plugin_file='/usr/lib/mysql/plugin/mysqlcft.so'





####cp SO file to mysql plugin root path 
#result=$(cp $mysqlcftpath $mysql_plugin_file)
#echo $result
initpluginsql='Install plugin mysqlcft soname "mysqlcft.so"'


####init SO file
#result=$(mysql -uroot  -s -e "${initpluginsql}")
#create database
create_sql="create database datap;"
#result=$(mysql -uroot  -s -e "${create_sql}")



####init database
init_sql="source $(pwd)/../spidermanage/sqldata/Dump20160803.sql"
#result=$(mysql -uroot  -s -e "${init_sql}")



####add user to database
adduser='use datap;insert into user_table values("admin123",3,3,"admin123")'
#result=$(mysql -uroot  -s -e "${adduser}")



#echo $result


#echo $result
#echo $mysqlcftpath
#for val in $result
#do
#   echo $val
#done


