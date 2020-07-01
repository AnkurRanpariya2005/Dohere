
ar=list(map(int,input().split()))
al=len(ar)	
count=0
r=[]

for i in range(al-1):
	a=ar[i+1]-ar[i]
	b=[]
	b=a
	if b==1:
		count+=1
	else:
		r.append(count+1)
		count=1
re=max(r)
if re>count:
	print(re)
else:
	print(count)



	
	
		
