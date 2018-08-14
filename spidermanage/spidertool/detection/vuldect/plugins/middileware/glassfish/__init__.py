KEYWORDS = ['glassfish', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    if 'resource/js/cj.js|glassfish.dev.java.net' in context:
        
        return True
    else:
        return False