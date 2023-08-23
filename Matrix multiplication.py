#Matrix Multiplication

A=[[1,2],[3,4]]
B=[[2,1],[3,2]]
C=[[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j]+=A[i][k]*B[k][j]
for k in C:
    print(k)
