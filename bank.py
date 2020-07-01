class Bank: 

	def __init__(self,Id,FName,SName,Amount): 
		self.Id=Id 
		self.FName=FName 
		self.SName=SName 
		self.Amount=Amount     

	def get(self,idd,fname,sname,amount):  
		ob=Bank(idd,fname,sname,amount) 
		save.append(ob)  

	def display(self,ob): 
		print("Id:",ob.Id) 
		print("FName:",ob.FName) 
		print("LName:",ob.SName) 
		print("Amount:",ob.Amount) 

	def search(self,fd):		
		for i in range(save.__len__()):
			if(save[i].Id==fd):
				return i
		
	def delete(self,fd):
		d=obj.search(fd)
		del save[d]
		
	def edit(self,fd):
		a=obj.search(fd)
		del save[a]
		return En
		ob=Bank(idd,fname,sname,amount) 
		save[i].Id==NO;
		
def pr():
	a=("Press Any Button \n A.Add Coustomer \n S.Display Coustomer Detail \n E.Edit Coustomer Detail \n DE.Delete Detail of Coustomer \n Q.Exit")
	print(a)
	
save=[] 
obj=Bank(0,"","",0) 

pr()

z=0

while z==0:

	btn=input("Enter your choose: ") 

	if (btn=="A"):
		En=obj.get(input("Enter Id:"),input("Enter FName:"),input("LName:"), input("Enter Amount:") )
		for i in range(save.__len__()):
			obj.display(save[i])
		pr()
		
	elif (btn=="D"):
		obj.delete(input("Enter Id:"))
		for i in range(save.__len__()):
			obj.display(save[i])
		pr()

	elif (btn=="E"):
		obj.edit(input())
		print(save.__len__())
		print("Edit")
		print("")
		En=obj.get(input("Enter Id:"),input("Enter FName:"),input("LName:"), input("Enter Amount:") )
		for i in range(save.__len__()):
			obj.display(save[i])
			print("Succesfully Edit")
		pr()
	
	elif (btn=="Q"):
		print("Thanks you")
	
	elif (btn=="S"):
		for i in range(save.__len__()):
			obj.display(save[i])
		pr()
	else:
		print("error")
	


