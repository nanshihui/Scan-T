#!/usr/bin/env python
# encoding: utf-8


class T(object):
    def __init__(self):

        self.result = {
                'type': None,
                'version': None,
                }
        self.keywords = []
        self.versions = []
    def match_rule(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo='', **kw):
##
#head 返回的请求头
#context　返回请求正文html代码
#ip　请求ip
#port 请求端口
#productname 请求的组件产品
#keywords 暂时已知的关键词组件
#hackinfo 备用字段
        
        
        
        
        return True

    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        result = {}
        result['result']=False
        return result
    def attack(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        result = {}
        result['result']=False
        return result
    def parse_output(self, result):
        result = {}
        result['result']=False
        return result