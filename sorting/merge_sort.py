# Base condition:  as long as len of arr > 1
# Break it into left and right and recurse until len or array > 1
# Soring happens in place, so you don’t need a new array.
# One while loop for i< len(left) and j < len(right), find which is greeted and merge
# Two while loops to add the remaining left and right into the array.

# Time Complexity: consistent O(n log n) time complexity. 
# Space Complexity: O(n), since it only requires temp arrays during merge.

# Bottom-up merge sort
# Let's illustrate the bottom-up merge sort with an example array [38, 27, 43, 3, 9, 82, 10]:
# Initial array as subarrays:
# [38],[27],[43],[3],[9],[82],[10]
# Merge Iteratively:
# Merge adjacent pairs: [27,38], [3,43], [9,82],[10]
# Merge adjacent pairs: [3,27,38,43],[9,10,82]
# Merge the last two remaining subarrays: [3,9,10,27,38,43,82]
# Sorted array: 3,9,10,27,38,43,82

def m_s_t(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        m_s_t(left)
        m_s_t(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                k+=1
                i+=1
            else:
                arr[k] = right[j]
                k+=1
                j+=1
        while i < len(left):
            arr[k] = left[i]
            k+=1
            i+=1
        while j < len(right):
            arr[k] = right[j]
            k+=1
            j+=1


    print(arr)


m_s_t([38, 27, 43, 3, 9, 82, 10])

def merge_sort_count(arr):
    global merge_count
    merge_count =0
    merge_sort_count_helper(arr)
    return merge_count


def merge_sort_count_helper(arr):
    global merge_count
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_count_helper(left)
        merge_sort_count_helper(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else:
                arr[k] = right[j]
                j+=1
                merge_count += len(left) - i #to find the merge count, we are looking for len(left) - i postion
                k+=1


        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1



# complexity is O(nlogn) in the best/average and worst case. Space complexity is O(n) as it requires temp space during merge
def merge_sort(arr):
   if len(arr) > 1:
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j = j+1
        k = k+1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# complexity is O(nlogn) in the best/average and worst case. Space complexity is O(n) as it requires temp space during merge


def bottom_up_merge_sort(arr):
    n = len(arr)
    temp_arr = [0]*n
    curr_size = 1

    while curr_size < n:
        left_start = 0
        while left_start < n - 1:
           mid = left_start + curr_size - 1
           right_end = min(left_start + 2 * curr_size - 1, n-1)

           merge(arr, temp_arr, left_start, mid, right_end)

           left_start += 2 * curr_size

        curr_size *= 2


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            i = i + 1
        else:
            temp_arr[k] = arr[j]
            j = j + 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
