KEYWORDS = ['zabbix', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
    if 'zabbix' in hackinfo or 'zabbix' in context:
        return True
    else:

        return False