#Diagonal sum

A=[[1,2,3],[4,5,7],[3,2,2]]
rows=len(A)
cols=len(A[0])
diagonal=0

for k in range(0,rows):
    diagonal+=A[k][k]
print("Sum of Diagonals is: ",diagonal)

    
