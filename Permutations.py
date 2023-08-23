#Permutations

import itertools
num=input("Enter the num: ")
p=list(itertools.permutations(num))
res=[' '.join(x)for x in p]
print(res)
