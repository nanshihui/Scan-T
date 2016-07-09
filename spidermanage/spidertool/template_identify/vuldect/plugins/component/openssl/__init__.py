KEYWORDS = ['heartblede', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    
    
    if int(port) in [443,587,465,995,8443] or productname.get('protocol','') in ['https','smtp','pop','imap','https-alt']:
        return True
    else:

        return False