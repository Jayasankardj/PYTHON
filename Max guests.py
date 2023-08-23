#Q2

def maxguests(E,L,T):
    max_guests=0
    current_guests=0
    for i in range(T):
        current_guests +=E[i]-L[i]
        if current_guests > max_guests:
            max_guests=current_guests
    return max_guests

E=[]
n=int(input("Enter the no.of hours: "))

for i in range(0,n):
    ele=int(input("Enter the element: "))
    E.append(ele)
print(E)

L=[]
a=int(input("Enter the no.of hours: "))

for i in range(0,a):
    ele=int(input("Enter the element: "))
    L.append(ele)

T=int(input("Enter the Time: "))
max_guests=maxguests(E,L,T)
print("Maximum number of guests on the cruise: ",max_guests)
