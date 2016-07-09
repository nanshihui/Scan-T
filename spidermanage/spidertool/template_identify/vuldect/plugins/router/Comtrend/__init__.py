KEYWORDS = ['comtrend', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):


	if 'comtrend' in context or 'comtrend' in head:
		return True
	else:
		return False