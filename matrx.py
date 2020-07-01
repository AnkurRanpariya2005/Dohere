import numpy as np
A=np.array([[3,4],[2,1]])
B=np.array([[1,5],[3,7]])
  
  
a=(A[0][0]*B[0][0])+(A[0][1]*B[1][0])
b=(A[1][0]*B[0][0])+(A[1][1]*B[1][0])


c=(A[0][0]*B[0][1])+(A[0][1]*B[1][1])
d=(A[1][0]*B[0][1])+(A[1][1]*B[1][1])

r=np.array([[a,c],[b,d]])

print(A,"\n")
print(B,"\n")
print("Result \n")
print(r)

