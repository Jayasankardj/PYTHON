#max len of string

s="python is high level language"
s1=s.split()
L=[]
for i in s1:
    L.append(len(i))
print(s1)
print(max(L))
