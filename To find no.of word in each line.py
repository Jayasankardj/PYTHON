#To find no.of word in each line

s=input("ENTER THE STRING: ")

lines=s.split(".")
lines.pop()
print("Number of lines: ",len(lines))
k=0
for i in lines:
    words=i.split()
    k+=1
    print("line",k,":",len(words))
