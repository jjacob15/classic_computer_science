# Selects a 'pivot' element, partitions the array into elements less than and greater than the pivot, and recursively sorts the partitions.
# Choose a Pivot: Select an element from the array to be the pivot. The choice of the pivot can vary: it can be the first element, the last element, the middle element, or even a random element.
# Partitioning: Rearrange the array such that all elements less than the pivot are on the left, and all elements greater than the pivot are on the right. The pivot element is now in its correct sorted position.
# Recursively Apply: Recursively apply the same process to the subarrays formed by partitioning, excluding the pivot element which is already in its correct position.
# Algo hints
# Base condition: low < high
# Select a pivot, generally the last value.
# Arranges the array where all the values lower than the pivot are on the left side.
# To do this, you iterate from low to high and check if the value in current position is < pivot
# If so, take an index set to low - 1, inc index and swap with the current value. 
# Finally take the i+1 and swap with pivot. This brings the pivot to the center and leave the high values to the right.
# Return i+1
# Call this function with low to partition index - 1  
# Call this function with partition index + 1 and high. 

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def partition(arr, low, high):
    print(low,high)
    pivot = arr[high]
    i = low - 1  # Initialize index of smaller element
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] < pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # Swap arr[i + 1] and arr[high] (or pivot)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
