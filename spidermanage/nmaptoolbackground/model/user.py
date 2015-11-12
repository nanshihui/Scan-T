#!/usr/bin/python
#coding:utf-8
class User(object):
    def __init__(self,username='',password='',role='',power=''):
        '''
        Constructor
        '''
        self.username=username
        self.password=password
        self.role=role
        self.power=power

    def setUsername(self,username):
        self.username=username
    def setPassword(self,password):
        self.password=password
    def setRole(self,role):
        self.role=role
    def setPower(self,power):
        self.power=power
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getRole(self):
        return self.role
    def getPower(self):
        return self.power
    