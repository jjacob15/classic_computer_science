def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)

def partition(arr, low, high):
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

