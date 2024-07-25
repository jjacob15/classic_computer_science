# Let's sort the array [5, 3, 8, 4, 2] using bubble sort:
# Initial array: [5, 3, 8, 4, 2]
# First Pass:
# Compare 5 and 3 -> swap -> [3, 5, 8, 4, 2]
# Compare 5 and 8 -> no swap -> [3, 5, 8, 4, 2]
# Compare 8 and 4 -> swap -> [3, 5, 4, 8, 2]
# Compare 8 and 2 -> swap -> [3, 5, 4, 2, 8]
# Second Pass:
# Compare 3 and 5 -> no swap -> [3, 5, 4, 2, 8]
# Compare 5 and 4 -> swap -> [3, 4, 5, 2, 8]
# Compare 5 and 2 -> swap -> [3, 4, 2, 5, 8]
# Compare 5 and 8 -> no swap -> [3, 4, 2, 5, 8]
# Third Pass:
# Compare 3 and 4 -> no swap -> [3, 4, 2, 5, 8]
# Compare 4 and 2 -> swap -> [3, 2, 4, 5, 8]
# Compare 4 and 5 -> no swap -> [3, 2, 4, 5, 8]
# Fourth Pass:
# Compare 3 and 2 -> swap -> [2, 3, 4, 5, 8]
# Compare 3 and 4 -> no swap -> [2, 3, 4, 5, 8]

# Time Complexity: O(n2) in the worst and average case, where n is the number of elements in the array. Quadratic time complexity
# Space Complexity: O(1), since it only requires a constant amount of additional space.

def bubble_sort(arr):

    swap = True
    while True:
        if not swap: break
        swap = False
        for i in range(len(arr)-2):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                swap = True

    return arr


