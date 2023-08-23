#sum of squares of first N natural numbers

n=int(input("Enter value of n: "))
sqr=0
sumsqr=0
for i in range(1,n+1):
    sqr+=(i**2)
    sumsqr+=i
print("Sum of square of first",n," natural numbers",sqr)
print("square of sum of first",n,"natural numbers",(sumsqr**2))
