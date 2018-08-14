KEYWORDS = ['xampp', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


    if 'xampp' in productname.get('protocol','') or 'xampp' in  productname.get('productname',''):

        return True
    else:

        return False