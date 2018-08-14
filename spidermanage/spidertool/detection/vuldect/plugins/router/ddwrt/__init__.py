KEYWORDS = ['ddwrt', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'ddwrt' in context or 'ddwrt' in head:
		return True
	else:
		return False