KEYWORDS = ['iis', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    if 'Microsoft-IIS' in head or  'Microsoft IIS httpd' in productname.get('productname',''):

        return True
    else:
        return False