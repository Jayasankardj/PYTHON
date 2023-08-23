#No.of rows & columns

A=[[1,2,3],[4,5,7],[3,2,2]]
rows=len(A)
cols=len(A[0])

#Rowsum
for i in range(0,rows):
    sumrow=0
    for j in range(0,cols):
        sumrow=sumrow+A[j][i]
    print("column",i+1,"is :",sumrow)
    
