import numpy as np

row = int(input("Enter the number of rows for Matrix1:")) 
row_cols = int(input("Enter the number of columns for Matrix1 and rows for Matrix2:")) 
Columns = int(input("Enter the number of columns for Matrix2:")) 

A = list(map(int, input().split())) 
B = list(map(int, input().split())) 
matrix=np.array(A).reshape(row,row_cols)
matrix1=np.array(B).reshape(row_cols,Columns)	

result=[[0 for i in range(row)] for j in range(Columns)]
re=result

		
for row in range(len(matrix)): #4
	for col in range(len(matrix1[0])): #4
		for k in range(len(matrix1)): #4
			re[row][col]+=matrix[row][k] * matrix1[k][col]

for r in re: 
    print(r)

