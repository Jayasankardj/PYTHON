#Print prime numbers in list

l=[1,2,3,4,5]
p=[]
c=[]
for num in l:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                c.append(num)
                break
            else:
                p.append(num)
print(p)
