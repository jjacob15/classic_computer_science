# Divides the array into a sorted and an unsorted region, repeatedly selects the smallest (or largest) element from the unsorted region, and moves it to the sorted region.
# Example
# Let's sort the array [5, 3, 8, 4, 2] using selection sort:
# Initial array: [5, 3, 8, 4, 2]
# First Pass:
# Find the minimum element in [5, 3, 8, 4, 2] -> 2
# Swap 2 with the first element -> [2, 3, 8, 4, 5]
# Second Pass:
# Find the minimum element in [3, 8, 4, 5] -> 3
# Swap 3 with the first element of the unsorted sublist (itself) -> [2, 3, 8, 4, 5]
# Third Pass:
# Find the minimum element in [8, 4, 5] -> 4
# Swap 4 with 8 -> [2, 3, 4, 8, 5]
# Fourth Pass:
# Find the minimum element in [8, 5] -> 5
# Swap 5 with 8 -> [2, 3, 4, 5, 8]

# complexity same as bubble sort

def selection_sort(arr):
    for i in range(len(arr)):
        mi = i
        for j in range(i,len(arr)):
            if arr[j] < arr[mi]:
                mi = j

        if mi == i: continue
        arr[i],arr[mi] = arr[mi],arr[i]

    return arr
