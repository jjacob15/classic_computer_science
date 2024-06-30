def remove_duplicate(sorted_arr):
    if not sorted_arr:
        return 0
    slow = 0
    for fast in range(1, len(sorted_arr)):
        if sorted_arr[fast] != sorted_arr[slow]:
            slow += 1
            sorted_arr[slow] = sorted_arr[fast]
    
    return sorted_arr[slow + 1:]

