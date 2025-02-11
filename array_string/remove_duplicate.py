#in a sorted array, remove duplicates
# have a slow and fast pointer.
# slow,fast = 0,1
# if slow == fast then move fast forward else, swap slow +1 with fast and increment slow, 
# the sorted array with be from slow+1

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

#insight -> the idea, keep fast one ahead, if they are NOT EQUAL, then increment slow by one and copy, NOT SWAP
# keep the slow at the current number and move fast until you find another number.
# increment slow and copy the fast over to the slow posiiton. slow now has the next number for fast to look out
# for
def remove_duplicate(arr):
    slow = 0
    for fast in range(1,len(arr)):
        if arr[slow] != arr[fast]:
            slow +=1
            arr[slow]= arr[fast]

    print(arr[:slow+1])


remove_duplicate([0,0,1,1,2,2,3,4,5,5])
















    # slow = 0
    # fast = 1
    # for fast in range(1,len(arr)):
    #     if arr[slow] != arr[fast]:
    #         slow +=1
    #         arr[slow]= arr[fast]

    # print(arr)