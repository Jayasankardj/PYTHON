def Goodpairs(nums):
    count=0
    for i in range(0,len(nums)):
        for j in range(0,i):
            if nums[i]==nums[j]:
                print("(",i,j,")")
                count+=1
    return count
l=[1,2,3,1,1,3]
print("No of GoodPairs: ",Goodpairs(l))
