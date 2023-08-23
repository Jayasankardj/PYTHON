#prime and composite

A=int(input("A= "))
B=int(input("B= "))
C,P=[],[]
for num in range(A,B+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                C.append(num)
                break
        else:
            P.append(num)
print("Prime:",P,len(P))
print("composite:",C,len(C))
