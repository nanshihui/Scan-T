#!/usr/bin/python
#coding:utf-8
def sipdeal(name):
    print 'this is sipdeal'
    pass
def sqldeal(name):
    print 'this is sqldeal'+name
def empty(name):
    print 'this is no method called  '+str(name)
 
 
    
portFunc = {'sip':sipdeal,'sql':sqldeal} 

