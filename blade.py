a=int(input())
t=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.sort()
y.sort()
p=0
for i in range(t):
	for j in range(p,t):
			