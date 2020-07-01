def arranged(array,start,end):
	p=array[start]	
	left=start+1
	right=end
	while True:
		while left<=right and array[left]<=p:
			left+=1
		while left<=right and array[right]>=p:
			right-=1
		if right<left:
			break
		else:
			array[left],array[right]=array[right],array[left]
			
	array[start],array[right]=array[right],array[start]
	return right
		
def partion(array,start,end):
	if start<end:
		loc=arranged(array,start,end)	
		partion(array,start,loc-1)
		partion(array,loc+1,end)

array=list(map(eval,input("Enter").split()))	
al=len(array)
partion(array,0,al-1)
print(array)
