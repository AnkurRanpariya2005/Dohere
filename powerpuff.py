print('Quantity of Indrients A')
A=(int(input('  ')))

print('Quantity of Indrients B')
B=(int(input('  ')))

print('Quantity of Indrients C')
C=(int(input('  ')))

print('Quantity of Indrients D')
D=(int(input('  ')))

w=2

x=5	#A indreinds require to make 							 powerpuff girl
y=6	#B indreinds require to make q						 powerpuff girl
z=3	#C indreinds require to make 						  powerpuff girl


p=A//w
q=B//x
r=C//y
s=D//z

result=[p,q,r,s]
print(min(result),'powerpuff girls is made')
