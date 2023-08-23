#string removing with given char

s=input("Enter a string; ")
char=input("Enter the character: ")

c=" "

for i in s:
    if i not in char:
        c=c+i
print(c)
