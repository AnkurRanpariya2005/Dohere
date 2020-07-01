a=2
lists=[1,31]
while a>0:
	offer=int(input())
	if offer<=30:
		lists.append(offer)
		li=lists.sort()
		print(lists)
	else:
		print('Invalid date')
	
	