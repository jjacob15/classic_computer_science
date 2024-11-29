# return yes if two numbers sum equals target
# INSIGHt -> using the target array value and a hash.
from collections import Counter
def two_sum(arr,target):
    c = Counter(arr)
    yes = False
    for i in range(len(arr)):
        if target - arr[i] in c:
            yes = True
            break

    if yes:
        print("YES")
    else:
        print("NO")
    
    
two_sum([2,6,5,8,11],15)