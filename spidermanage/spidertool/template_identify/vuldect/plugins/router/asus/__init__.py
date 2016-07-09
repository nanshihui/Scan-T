KEYWORDS = ['asus', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'asus' in context or 'asus' in head:
		return True
	else:
		return False