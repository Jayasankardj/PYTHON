#python program for matrix

a=[[3,7,4],[10,1,2],[8,9,6]]
b=[]
l=[]
for i in a[0]:
    b.append(i)
for i in range(len(a)):
    b.append(a[i][2])
for i in range(-1,len(a)-1,-1):
    b.append(a[2][i])
for i in a[1]:
    b.append(l)
for i in b:
    if i not in l:
        l.append(i)
print(l)
