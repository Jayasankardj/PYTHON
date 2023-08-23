#Matrix Addition

A=[[1,2],[3,4]]
B=[[2,1],[3,2]]
C=[[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
            C[i][j]=A[i][j]+B[i][j]
for k in C:
    print(k)
