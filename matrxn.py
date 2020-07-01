import numpy as np

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

A = list(map(int, input().split())) 
B = list(map(int, input().split())) 
result = [[0, 0,], 
        [0, 0]]
matrix=np.array(A).reshape(R, C)
matrix1=np.array(B).reshape(R, C)	

for i in range(len(matrix)): 
	for j in range(len(matrix1)): 
		for k in range(len(matrix1)):
			result[i][j] = (matrix[i][k] * matrix1[k][j] )+result[i][j] 
  
for r in result: 
    print(r)


