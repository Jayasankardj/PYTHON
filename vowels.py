#vowels

s="Temple Tower"
vowels="AaEeIiOoUu"
v,c=0,0
for i in s:
    if i.isalpha():
        if i in vowels:
            v+=1
        else:
            c+=1
print("vowels: ",v)
print("consonents: ",c)
