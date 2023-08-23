#Matrix

a=[[3,4,5],[7,8,9,],[10,11,12]]
rows=len(a)
col=len(a[0])

for i in range(0,rows):
    sumrow=0
    for j in range(0,col):
        sumrow+=a[i][j]
    print("ROW",i+1,"is: ",sumrow)
for x in range(0,rows):
    sumcol=0
    for y in range(0,col):
        sumcol+=a[y][x]
    print("coloumn",x+1,"is: ",sumcol)
diagonal=0
for k in range(0,rows):
    diagonal +=a[k][k]
print("Sum of diagonal is : ",diagonal)
