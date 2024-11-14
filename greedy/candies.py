# Alice is a kindergarten teacher. She wants to give some candies to the children in her class. 
# All the children sit in a line and each of them has a rating score according to his or her performance in the class.
# Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating
#  must get more candies. Alice wants to minimize the total number of candies she must buy.

# arr = [4,6,4,5,6,2]
# she should give [1,2,1,2,3,1], so total it to 10 candies.

# INSIGHT -> the first pass increments the candy by one of the last child. This does not account for imbalances so, reverse the order
# and check if the adjacent two children needs to be adjusted.


def candies(arr):
    r = [1]*len(arr)

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            r[i] = r[i-1]+1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > arr[i+1] and r[i]<=r[i+1]:
            r[i]=r[i+1]+1
   
    return sum(r)