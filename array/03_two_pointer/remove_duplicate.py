#in a sorted array, remove duplicates
# have a slow and fast pointer.
# slow,fast = 0,1
# if slow == fast then move fast forward else, swap slow +1 with fast and increment slow, the sorted array with be from slow+1
def remove_duplicate(arr):
    if len(arr) == 1:
        return arr
    
    slow = 0
    fast = 1
    while fast < len(arr):
        if arr[slow] == arr[fast]:
            fast+=1
        else:
            arr[slow+1] = arr[fast]
            slow +=1 

    return arr[:slow+1]