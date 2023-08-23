#Q-3

a=input("Enter text: ")
letters=[]

for i in a:
    letters.append(i)

vowels="AEIOUaeiou"
l=[]
for j in letters:
    if j.isalpha:
        if j in vowels:
            l.append(j)
            l.append("$")
        else:
            l.append(j)
            l.append("+")
print(*l)
