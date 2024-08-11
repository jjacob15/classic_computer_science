# Builds the final sorted array one item at a time, inserting each new item into its proper 
# place among the already-sorted items.

# Example
# Let's sort the array [5, 3, 8, 4, 2] using insertion sort:
# Initial array: [5, 3, 8, 4, 2]
# First Pass:
# Key: 3
# Compare 3 with 5, shift 5 to the right -> [5, 5, 8, 4, 2]
# Insert 3 at the correct position -> [3, 5, 8, 4, 2]
# Second Pass:
# Key: 8
# Compare 8 with 5, no shift needed -> [3, 5, 8, 4, 2]
# Third Pass:
# Key: 4
# Compare 4 with 8, shift 8 to the right -> [3, 5, 8, 8, 2]
# Compare 4 with 5, shift 5 to the right -> [3, 5, 5, 8, 2]
# Insert 4 at the correct position -> [3, 4, 5, 8, 2]
# Fourth Pass:
# Key: 2
# Compare 2 with 8, shift 8 to the right -> [3, 4, 5, 8, 8]
# Compare 2 with 5, shift 5 to the right -> [3, 4, 5, 5, 8]
# Compare 2 with 4, shift 4 to the right -> [3, 4, 4, 5, 8]
# Compare 2 with 3, shift 3 to the right -> [3, 3, 4, 5, 8]
# Insert 2 at the correct position -> [2, 3, 4, 5, 8]
# Algo hints
# Start from the second item and key going forward.
# Use a while loop to iterate and update the sorted sub list as you go forward 
# When that loop ends, update the key there.


# complexity same as bubble sort

def insertion_sort(arr):
    n = len(arr) -1
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr