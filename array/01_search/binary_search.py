# Efficiently finds an element in a sorted array by repeatedly dividing the search interval in half. 
# Mid = (low + high))//2
# Loop while low <= high
# Return index if found or -1

# Time Complexity: O(log⁡n) for worst-case, best-case, and average-case scenarios.
# Space Complexity: O(1) for the iterative version and O(log⁡n) for the recursive version.

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

