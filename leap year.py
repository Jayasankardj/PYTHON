#leap year

d=input("Enter the date in format of DD/MM/YY : ")
s=d.split("/")
n=int(s[-1])

if n%400==0:
    if n%100==0:
        if n%4==0:
            print(d,"Is a Leap year")
        else:
            print(d,"Not a Leap year")
    else:
        print(d,"Is a Leap year")
else:
    print(d,"Not a Leap year")
    
    
