#Matrix Transpose

A=[[1,2],[3,4]]

C=[[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(A)):
            C[i][j]=A[j][i]
for k in C:
    print(k)
