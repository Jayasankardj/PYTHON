#factors

num=int(input("Enter: "))
L=[]
for i in range(1,num):
    if num%i==0:
        L.append(i)
print(L)
