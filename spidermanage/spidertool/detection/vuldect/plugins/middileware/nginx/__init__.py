KEYWORDS = ['nginx', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    if 'nginx' in  hackinfo or 'nginx' in head :
        return True
    else:
        return False