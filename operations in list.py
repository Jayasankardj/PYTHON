l=[3,8,-2,-4,-1,5]
l.sort()
print("Largest number: ",l[-1])
print("Smallest number: ",l[0])
a,b,c=0,0,1
for i in l:
    a+=i
    b-=i
    c*=i
print("Sum of numbers: ",a)
print("Difference of numbers: ",b)
print("Product of numbers: ",c)

