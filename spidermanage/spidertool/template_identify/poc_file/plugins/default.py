#!/usr/bin/env python
# encoding: utf-8


from os.path import dirname, abspath, join, isdir
from os import listdir
from urlparse import urljoin
from re import compile
import callbackresult



class PocController(object):
    def __init__(self, logger=None):
        self.modules_list = [

                {'module_name': 'component'},
 ]


        self.keywords    = {}
        self.components     = {}
        self.logger      = logger
        self.result=None
        self.loader()
    def __list_plugins(self, module_path):
        return set(map(lambda item: item.endswith(('.py', '.pyc')) and item.replace('.pyc', '').replace('.py', ''), listdir(module_path)))

    def __get_component_plugins_list(self,componentname, module_name):
        path = join(abspath(dirname(__file__)), componentname+'/%s' % module_name)
        plugins_list = self.__list_plugins(path)
        if False in plugins_list:
            plugins_list.remove(False)
        plugins_list.remove('__init__')
        if 't' in plugins_list:
        
            plugins_list.remove('t')
        return plugins_list
    def __get_component_detail_list(self,componentname):
        path = join(abspath(dirname(__file__)), componentname)
        modules_list = set(map(lambda item: isdir(join(path, item)) and item, listdir(path)))
        if False in modules_list:
            modules_list.remove(False)


        return modules_list
    def __load(self, module_name, plugin_name):

        plugin_name = '%s.%s' % (module_name, plugin_name)

        plugin = __import__(plugin_name,globals=globals(), fromlist=['P'])

        self.logger and self.logger.info('Load Plugin: %s.P', plugin_name)
        return plugin.P
    def __load_keywords(self,componentname, module_name):
        module_name = componentname+'.%s' % (module_name)

        module = __import__(module_name,globals=globals(), fromlist=['KEYWORDS'])
        return module.KEYWORDS,componentname
    def __load_component_detail_plugins(self, componentname=''):

        modules_list = self.__get_component_detail_list(componentname)
        for module_name in modules_list:
            self.components[componentname][module_name] = []

            for plugin_name in self.__get_component_plugins_list(componentname,module_name):
                
                P = self.__load(componentname+'.%s' % module_name, plugin_name)
                self.components[componentname][module_name].append(P)
                try:

                    self.keywords[module_name] = self.__load_keywords(componentname,module_name)
                    self.logger and self.logger.info('Module Keywords: %s -> %s', module_name, self.keywords[module_name])
                except:
                    self.keywords[module_name] = [],componentname
                    self.logger and self.logger.info('Module Keywords: %s -> None', module_name)
                    pass
    def __load_component_plugins(self, modules_list):
        for module_name in modules_list:
            self.components[module_name] = {}
            self.__load_component_detail_plugins(module_name)

    def loader(self):
        self.components = {}
        self.__load_component_plugins(map(lambda module_info: module_info['module_name'], self.modules_list))
    def env_init(self, head='',context='',ip='',port='',productname='',keywords='',hackinfo=''):
        self.init(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)
    def init(self,  head='',context='',ip='',port='',productname='',keywords='',hackinfo='', **kw):
        POCS = []
        modules_list = []
        
        
        modules_list, _ = self.__match_modules_by_keywords(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords)
        
        for modules,conponent in modules_list:
            for item in self.components[conponent][modules]:
                P=item()
                POCS.append(P)
                self.logger and self.logger.info('Init Plugin: %s', item)
        self.match_POC(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo,POCS=POCS, **kw)
    def match_POC(self,head='',context='',ip='',port='',productname='',keywords='',hackinfo='',POCS=None, **kw):
        haveresult=False
        for poc in POCS:

            result = poc.verify(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)
            print result

            if result['result']:
                haveresult=callbackresult.storedata(ip=ip,port=port,hackinfo=result)
                print '发现漏洞'
                break;


        if haveresult == False:
            print '-----------------------'
            print '暂未发现相关漏洞'
    def __match_modules_by_keywords(self,head='',context='',ip='',port='',productname='',keywords=''):
        matched_modules = []
        othermodule=[]
#         for module_name in self.components.keys():
#             othermodule.extend(self.components[module_name].keys())

        kw=keywords#关键词

        for module_name, module_info in self.keywords.items():

            keywords=module_info[0]
            comonentname=module_info[1]
            if not keywords:
                matched_modules.append([module_name,comonentname])
                continue
            for keyword in keywords:
                if keyword in kw or keyword in productname.lower()  or keyword in head.lower()   :
                    
                    
#                     self.logger and self.logger.info('Match Keyword: %s -> %s', resp.url, keyword)
                    matched_modules.append([module_name,comonentname])
                    break
# 
#         for match in matched_modules:
#             othermodule.remove(match)
#         print othermodule
        return matched_modules, othermodule



    def detect(self, head='',context='',ip='',port='',productname='',keywords='',hackinfo=''):


        self.env_init(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)
# 
# 
# 
#         self.__detect(resp)
        return

