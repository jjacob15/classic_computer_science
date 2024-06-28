#its O(n2) due to the nested loop
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(arr[i:]):
            if arr[i]> arr[j]:
                arr[j],arr[i] = arr[i], arr[j]
    return arr


