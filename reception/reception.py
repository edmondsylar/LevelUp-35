def registration_checker(name):
	vip = open("../vip_list.txt", "r+")
	ord_n = open("../ordinary_list.txt")

	vip_members = []
	ordinary = []

	for name in vip:
		vip_members.append(name.rstrip('\n'))

	for name in ord_n:
		ordinary.append(name.rstrip('\n'))

	for i in ordinary:
		if username not in i:
			continue
		elif username in i:
			print ('{}, Ordinary'.format(i))
		else:
			print ('Not registered')

	for i in vip_members:
		if username not in i:
			continue
		elif username in i:
			return ('{}, VIP'.format(i))
		else:
			print ('Not registered')

	if username not in ordinary or vip_members:
		pass

	else:
		return 'Not exist'

username = raw_input('Enter name:: ')

registration_checker(username)
			

