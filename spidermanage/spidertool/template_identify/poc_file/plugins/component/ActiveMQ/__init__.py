KEYWORDS = ['activemq', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


    if 'jdwp' in productname.get('activemq','') or 'Apache ActiveMQ' in  productname.get('productname',''):
        return True
    else:

        return False