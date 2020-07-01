au=list(map(str,input().split()))
n=list()
for au in au:
  number = ord(au)-96
  n.append(number)
al=len(n)	
count=0
r=[]

for i in range(al-1):
	a=n[i+1]-n[i]
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



	
	
		
