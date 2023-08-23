#Armstrong
num=int(input("Enter: "))

temp=num
sum=0
while temp>0:
    z=temp%10
    sum=sum+(z**3)
    temp=temp//10
print(sum)
