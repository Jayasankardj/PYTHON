#factors for n digits

n=int(input("Enter N: "))
num=int(input("Enter: "))
L=[]
for i in range(1,num):
    if num%i==0:
        L.append(i)
print("Factors of the number are: ",L)

l=[]
for j in range(1,n+1):
    if n%j==0:
        l.append(j)
        if len(l)==n:
            break
        
print("Factors of the number are: ",l)


