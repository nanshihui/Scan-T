KEYWORDS = ['d-link', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'd-link' in context or 'd-link' in head:
		return True
	else:
		return False