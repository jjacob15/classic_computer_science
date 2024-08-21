# For an array [2,4,2,6,1,7,8,9,2,1] you give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must
# get more candies. but from 9 to 1 you end up giving only one candy. TO FIX THAT YOU HAVE A TWO PASS SOLUTION.
# INSIGHT -> the first pass increments the candy by one of the last child. in the reverse case, check if the two adjacent student the same or lesser 
# candy and increment that.

def candies(arr):
    r = [1]*len(arr)

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            r[i] = r[i-1]+1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > arr[i+1] and r[i]<=r[i+1]:
            r[i]=r[i+1]+1
   
    return sum(r)