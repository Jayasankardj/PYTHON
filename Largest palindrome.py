#Largest palindrome

n=0
for a in range(999,100,-1):
    for b in range(100,a,-1):
        x=a*b
        if x>n:
            s=str(a*b)
            if s==s[::-1]:
                n=a*b
print(a,"*",b,"=",n)
