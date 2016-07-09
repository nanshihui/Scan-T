KEYWORDS = ['httpfileserver', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    if 'HttpFileServer' in  productname.get('productname',''):
        return True
    else:
        return False