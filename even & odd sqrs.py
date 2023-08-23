l=[2,3,4,5,6,7,8,9]
e,o=0,0
for i in l:
    if (i%2==0):
        e+=i
    else:
        o+=i
print("Even square: ",e**2)
print("Odd square: ",o**2)
