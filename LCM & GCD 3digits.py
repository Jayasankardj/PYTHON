from math import gcd
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

gcd_abc=gcd(a,b,c)
print("GCD of the numbers: ",gcd_abc)
lcm=(a*b*c)/gcd_abc
print("LCM of the numbers: ",lcm)
