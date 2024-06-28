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

