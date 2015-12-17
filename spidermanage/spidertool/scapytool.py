#! /usr/bin/env python
#coding:utf-8
from scapy.all import *
from scapy.modules.p0f import prnp0f, p0f
load_module('p0f')
# p=sniff(iface="eth0",count=3,store=0)
# print p[0].show()


def monitor_callback(pkt):
    print '----------------------------------'
#     print pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}")

#     prnp0f(pkt)
#     print pkt[0]

    
#     hexdump(pkt)
#     p0f(pkt)#要判断参数是否为icp包

#     print pkt.show()
    if Ether in pkt:
        print pkt[Ether].src+'----->'+pkt[Ether].dst
    if IP in pkt:
        print pkt[IP].src+':'+str(pkt[IP].sport)+'----->'+pkt[IP].dst+':'+str(pkt[IP].dport)
    if Raw in pkt:
        print pkt[Raw].load
    if Padding in pkt:
        print pkt[Padding].load
    print '---------------------------------'
sniff(prn=monitor_callback, store=0)









