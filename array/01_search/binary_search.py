# Efficiently finds an element in a sorted array by repeatedly dividing the search interval in half. 
# Mid = (low + high))//2
# Loop while low <= high
# Return index if found or -1

# Time Complexity: O(log⁡n) for worst-case, best-case, and average-case scenarios.
# Space Complexity: O(1) for the iterative version and O(log⁡n) for the recursive version.
# INSIGHT -> can not only be used to find the an item in a sorted array, you could use it to find
# the count of elements less than or greater than the target. Change the condition to arr[mid] <=item 
# and the position of l will give you that

# INSIGHT -> when you are finding the count of items lesser than or greater than in the arr, the bound and the l and r position changes.
# Make sure the upper bound is len(arr) as you might want to include the last value as well.
# for finding the item lesser than the target, make sure the r = mid. DON'T subtract here. 
# for finding the item greater than the target, make sure the l = mid. DON'T add here. 

# INSIGHT -> when using binary search looking for bounds.
# the upper bound of high or r can be len(arr) - 1 or len(arr) depending on what you are trying to acheive. WHEN YOU ARE SEARCHING 
# FOR A SPECFIC VALUE/ELEMENT EXISTS USING LEN(ARR) -1 
# WHEN YOU ARE FIND THE INTERSECTION POINT, UPPER OR LOWER BOUND, NUMBER OF ITEMS LOWER THAN, YOU USE LEN(ARR). Its because the value might be 
# beyond the upper bound of the array.

def binary_search(arr, item):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == item:
            return mid
        elif item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

