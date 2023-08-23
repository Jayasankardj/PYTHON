#Nth largest & Mth largest sum,difference,product

l=[2,3,5,7,4]
l.sort()
x=int(input("nth smallest: "))
y=int(input("mth largest: "))

print("smallest number is: ",l[x-1])
print("largest number is: ",l[-y])

print("sum: ",l[x-1]+l[-y])
