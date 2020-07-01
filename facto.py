def main():
		facto(input())
		
def validate1(a):
		try:
			if '.' in a:
				return False
			if int(a)<=0:
				return False
			return True
		except:
			return False
			
def facto(n):
	x=validate1(n)
	if (x):
		r=1
		for i in range(int(n),0,-1):
			r=r*i
		print(r)
	else:
		print("invald")

main()


				
			
      
	




			
			






		


