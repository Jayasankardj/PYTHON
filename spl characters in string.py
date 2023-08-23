#spl characters in string

str1="*python slot-D @ 401"
a,d,sp,spl=0,0,0,0
alpha,digit,space,special=[],[],[],[]
for i in range(len(str1)):
    if str1[i].isalpha():
        a+=1
        alpha.append(str1[i])
    elif str1[i].isdigit():
        d+=1
        digit.append(str1[i])
    elif str1[i].isspace():
        sp+=1
    else:
        spl+=1
        special.append(str1[i])
print("Alphabets: ",alpha,a)
print("Digits: ",digit,d)
print("Space: ",sp)
print("Special: ",special,spl)

    
