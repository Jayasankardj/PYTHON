l=[1,2,3,-1,1,3]
sum=0
for i in range(len(l)):
    sum+=l[i]
avg=sum/len(l)

for j in range(len(l)):
    if l[j]<0:
        l[j]=avg
print(sorted(l))
