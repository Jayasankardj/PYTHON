#Functions for string operations

s1= input("Enter string 1: ")
s2= input("Enter string 2: ")

s3=""
for i in range(min(len(s1),len(s2))):
    s3+=s1[i]
    s3+=s2[i]
print(s3)
