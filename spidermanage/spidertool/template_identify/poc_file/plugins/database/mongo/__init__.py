KEYWORDS = ['mongo', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


    if '27017' in port :
        return True
    else:

        return False