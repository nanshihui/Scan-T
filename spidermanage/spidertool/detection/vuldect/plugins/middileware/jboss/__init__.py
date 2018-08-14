KEYWORDS = ['jboss', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    if 'youcandoit.jpg' in context or 'JBossWeb'in context or 'jboss' in hackinfo or 'jboss' in head :
        return True
    else:
        return False