KEYWORDS = ['cgi', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    
    
    if 'cgi-bin' in hackinfo or 'cgi-bin' in  context:
        return True
    else:

        return False