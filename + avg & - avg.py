l=[3,6,9,-2,-4,-8]
p,n,j,k=0,0,0,0
for i in l:
    if (i>0):
        p+=i
        j+=1
    else:
        n+=i
        k+=1

avg1=p/j
avg2=n/k

print(avg1)
print(avg2)





