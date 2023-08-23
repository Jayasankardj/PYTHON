n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
x=n1
y=n2
while n2!=0:
    t=n2
    n2=n1%n2
    n1=t
gcd=n1
print("GCD of the numbers: ",gcd)
lcm=(x*y)/gcd
print("LCM of the numbers: ",lcm)
