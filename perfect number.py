#perrfect numbers

sum=0
num=int(input("Enter: "))
L=[]
for i in range(1,num):
    if num%i==0:
        L.append(i)
        sum+=i
if sum==num:
    print("Perfect number")
else:
    print("Not a perfect number")
    
