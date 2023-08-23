#remove duplicates from array

l=[2,3,4,5]
l1=[2,5,9,3]
for i in range(len(l1)):
    if l.count(l[i])>1:
        continue
    else:
        l1.append(l[i])
print(l1)
