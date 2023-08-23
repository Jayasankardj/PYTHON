#Sum of the digits

n=int(input("Enter a number: "))
sum=0
z=0
while n>0:
    z=n%10
    sum=sum+z
    n=n//10
print("The sum of digits is ",sum)
