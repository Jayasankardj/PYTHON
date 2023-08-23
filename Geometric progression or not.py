#Geometric progression or not

def geometric(lst):
    if len(lst)<3:
        return False
    ratio=lst[1]/lst[0]

    for i in range(2,len(lst)):
        if lst[i]/lst[i-1]!=ratio:
            return False
    return True

lst=input("Enter a list of numbers seperated by comas: ")
lst=[float(x.strip()) for x in lst.split(",")]
if geometric(lst):
    print("list is in Gp ")
else:
    print("list is not in GP")

print("Common ratio is : ",lst[1]/lst[0])
