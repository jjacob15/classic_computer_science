# INSIGHT -> a  high pivot, or a point where you take all values lower than the pivot and swap them with the lower pointer.
def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
    print(arr)

def quick_sort_helper(arr,low,high):
    if low <high:
        pi = partition(arr,low,high)
        quick_sort_helper(arr,low,pi-1) # you take partition index -1 and 
        quick_sort_helper(arr,pi+1,high) # you take partition index + 1 to exclude the pivot
    

def partition(arr,low,high):
    pivot = arr[high]
    i = low 
    for j in range(low,high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[high] = arr[high],arr[i]
    return i

quick_sort([7,12,4,2,67,9,45,1,6,56,3,234])
quick_sort([10,9,8,7,6,5,4,3,2,1])
# quick_sort([4,6,2,5,7,9,1,3])