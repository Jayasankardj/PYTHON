

s=[]
while True:
    n=input("Enter string: ")
    if n==-1:
        break
    else:
        s.append(n)
print(s)   
dig=[]
alp=[]
space=[]
spl=[]

for i in s:
    if i.isdigit():
        dig.append(i)
    elif i.isalpha():
        alp.append(i)
    elif i.isspace():
        space.append(i)
    else:
        spl.append(i)
print("No of number in list are: ",len(dig))
print("No of special characters in list are: ",len(spl))

