KEYWORDS = ['weblogic', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    if 'Hypertext Transfer Protocol' in context or 'console/css/login.css|Login_GC_LoginPage_Bg.gif' in context or 'weblogic' in hackinfo or 'weblogic' in keywords or 'weblogic' in productname.get('productname',''):
        
    
        return True
    
    else:
    
        return False