#sum of N digits

num=int(input("Enter: "))

temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
print(sum)
