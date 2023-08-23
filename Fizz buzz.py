n=int(input("Enter a number: "))
s=[]
for i in range(1,n+1):
    if (i%3==0 and i%5==0):
        print("Fizz Buzz")
    elif (i%5==0):
        print("Buzz")
    elif (i%3==0):
        print("Fizz")
    else:
        s.append(i)
print(s)    
