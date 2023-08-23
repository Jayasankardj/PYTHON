#printing first letter of each word

s="This is a cat"
s1=s.split()
for i in range(len(s1)):
    print(s1[i][0].upper(),end=" ")
    
