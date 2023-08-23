#string replacing with #

s=input("Enter a string; ")
char=input("Enter the character: ")

c=" "

for i in s:
    if i not in char:
        c=c+i
    else:
        c=c+"#"
print(c)
