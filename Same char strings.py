#same char strings

s1=input("Enter the string: ")
s2=input("Enter the string: ")

c=0
if len(s1)<=len(s2):
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            c+=1
else:
    for i in range(len(s2)):
        if s2[i]==s1[i]:
            c+=1
print(c)
