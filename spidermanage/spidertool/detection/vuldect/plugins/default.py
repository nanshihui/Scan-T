#!/usr/bin/env python
# encoding: utf-8


from os.path import dirname, abspath, join, isdir
from os import listdir
from urlparse import urljoin
from re import compile
import callbackresult
GPocController=None
def getObject():
    global  GPocController
    if  GPocController is None:
        GPocController=PocController()
        GPocController.loadonce()
    return GPocController.getitem()

class PocController(object):
    def __init__(self, logger=None):
        self.modules_list = [

            {'module_name': 'component'},
            {'module_name': 'middileware'},
            {'module_name': 'database'},
            {'module_name': 'basemodel'},
            {'module_name': 'router'},
            {'module_name': 'thirdparty'}
 ]


        self.keywords    = {}
        self.rules    = {}
        self.components     = {}
        self.logger      = logger
        self.result=None

        self.loadonce()
    def getitem(self):
        return self.keywords,self.rules,self.components
    def loadonce(self):
        self.loader()
    @classmethod
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
        if 'miniCurl' in plugins_list:
            plugins_list.remove('miniCurl')
        return plugins_list

    @classmethod
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

    @classmethod
    def __load_keywords(self,componentname, module_name):
        module_name = componentname+'.%s' % (module_name)

        module = __import__(module_name,globals=globals(), fromlist=['KEYWORDS'])
        return module.KEYWORDS,componentname

    @classmethod
    def __load_rules(self,componentname, module_name):
        module_name = componentname+'.%s' % (module_name)
        module = __import__(module_name,globals=globals(), fromlist=['rules'])
        return module.rules,componentname    
    def __load_component_detail_info(self,module_name='',componentname='',func=None,params=None,text=''):
        try:

            params[module_name] = func(componentname,module_name)
            self.logger and self.logger.info('Module '+text+': %s -> %s', module_name, self.keywords[module_name])
        except Exception,e:
            print e
            params[module_name] = [],componentname
            self.logger and self.logger.info('Module '+text+': %s -> None', module_name)
            pass
    def __load_component_detail_plugins(self, componentname=''):

        modules_list = self.__get_component_detail_list(componentname)
        for module_name in modules_list:
            self.components[componentname][module_name] = []

            for plugin_name in self.__get_component_plugins_list(componentname,module_name):
                
                P = self.__load(componentname+'.%s' % module_name, plugin_name)
                self.components[componentname][module_name].append(P)
                self.__load_component_detail_info(module_name=module_name,componentname=componentname,func=self.__load_keywords,params=self.keywords,text='keywords')
                self.__load_component_detail_info(module_name=module_name,componentname=componentname,func=self.__load_rules,params=self.rules,text='rules')
    def __load_component_plugins(self, modules_list):
        for module_name in modules_list:
            self.components[module_name] = {}
            self.__load_component_detail_plugins(module_name)

    def loader(self):
        self.components = {}
        self.__load_component_plugins(map(lambda module_info: module_info['module_name'], self.modules_list))
    def env_init(self, head='',context='',ip='',port='',productname=None,keywords='',hackinfo='',defaultpoc=''):
        self.init(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo,defaultpoc=defaultpoc)
    def __match_modules_by_poc(self,head='',context='',ip='',port='',productname=None,keywords='',defaultpoc=''):
        matched_modules = set()
        othermodule=[]

        for components_name in self.components.keys():
            for module_name in self.components[components_name].keys():
                if module_name in defaultpoc:
                    matched_modules.add((module_name,components_name))


        return matched_modules, othermodule
    def init(self,  head='',context='',ip='',port='',productname=None,keywords='',hackinfo='', defaultpoc='',**kw):
        POCS = []
        modules_list = []
        
        if defaultpoc=='':
            modules_list, _ = self.__match_modules_by_info(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)
        else:
            
            modules_list, _ = self.__match_modules_by_poc(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,defaultpoc=defaultpoc)
        print ' 匹配到的可能组件:      '+str(modules_list) 
        for modules,conponent in modules_list:
            for item in self.components[conponent][modules]:
                P=item()
                try:
                    if self.__match_rules(pocclass=P,head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo, **kw):
                        POCS.append(P)
                except Exception,e:
                    self.logger and self.logger.info('error: %s', e)
                
                
        
                self.logger and self.logger.info('Init Plugin: %s', item)
        print ' 要执行筛选的组件:      '+str(POCS) 
        self.match_POC(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo,POCS=POCS, **kw)

    @classmethod
    def match_POC(self,head='',context='',ip='',port='',productname=None,keywords='',hackinfo='',POCS=None, **kw):
        haveresult=False
        dataresult=[]
        result={}
        i=0
        for poc in POCS:

            try:
                result = poc.verify(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo)

                if type(result) == dict:
                    if result['result']:
                        i = 1
                        dataresult.append(result)

                        print '发现漏洞'



            except Exception,e:
                print e,poc


            else:
                pass
        if i==1:
            
            callbackresult.storedata(ip=ip,port=port,hackinfo=dataresult)
            # callbackresult.storeresult(dataresult)
            pass
        else:
            print '-----------------------'
            print '暂未发现相关漏洞'
        del POCS

    @classmethod
    def __match_rules(self,pocclass=None,head='',context='',ip='',port='',productname=None,keywords='',hackinfo='', **kw):

        return pocclass.match_rule(head='',context='',ip='',port='',productname=productname,keywords='',hackinfo='', **kw)
        
    
    
    
    
    
    
    def __match_modules_by_info(self,head='',context='',ip='',port='',productname=None,keywords='',hackinfo=''):
        matched_modules = set()
        othermodule=[]
#         for module_name in self.components.keys():
#             othermodule.extend(self.components[module_name].keys())
        if (productname is not None and productname.get('productname',None) is None):
            productname['productname']=''
        if head ==None:
            head=''
        if hackinfo ==None:
            hackinfo=''

        kw=keywords#关键词
        for module_name, module_info in self.keywords.items():
            modulekeywords=module_info[0]
            comonentname=module_info[1]
            if not modulekeywords:
                
                
                matched_modules.add((module_name,comonentname))
                continue
            for keyword in modulekeywords:
                if keyword in kw or keyword in productname.get('productname','').lower()  or keyword in head.lower() or keyword in hackinfo.lower()    :
                    
                    
#                     self.logger and self.logger.info('Match Keyword: %s -> %s', resp.url, keyword)
                    matched_modules.add((module_name,comonentname))
                    break
        for module_name, module_info in self.rules.items():
            rules=module_info[0]
            comonentname=module_info[1]

            if not rules:
                

                matched_modules.add((module_name,comonentname))
                continue
            if rules(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo='')  :
                     
                     
                matched_modules.add((module_name,comonentname))
#             matched_modules.add((module_name,comonentname))
                    

        return matched_modules, othermodule



    def detect(self, head='',context='',ip='',port='',productname={},keywords='',hackinfo='',defaultpoc=''):
        # self.logger and self.logger.info('now the source component: %s', self.components)

        if self.components=={} or self.keywords == {} or self.rules=={}:

            self.loader()

        self.env_init(head=head,context=context,ip=ip,port=port,productname=productname,keywords=keywords,hackinfo=hackinfo,defaultpoc=defaultpoc)

        return

if __name__ == "__main__":

    a=PocController()
    a.detect(ip='202.121.168.201',port='9000',context='zabbix')