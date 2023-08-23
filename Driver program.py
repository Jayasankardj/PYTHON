#Driver program
#1!/1+2!/2+3!/3+4!/4+5!/5

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input("Enter a Number: "))
sum=0
for i in range(1,n+1):
    sum=sum+fact(i)/i
print(sum)
