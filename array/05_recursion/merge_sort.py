# T 0(nlogn) ->  when you recursively call n/2 16 -> 8,8 ->4,4,4,4 etc. This means its log2(n) and at max you will have n merges therefore nlogn
# space complexity nlogn because you are creating 
def merge_sort(arr):
    n = len(arr)
    if n <=1: return 
    mid = n//2

    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)

    # wait till it reaches the bottom of the tree and then backtrack with the arr and elements and merge
    i=j=k =0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1
    while i < len(left):
        arr[k] = left[i]
        k+=1
        i+=1

    while j < len(right):
        arr[k] = right[j]
        k+=1
        j+=1
    

# arr = [6,5,4,3,2,1]
# merge_sort(arr)   
#INSIGHT using pointers.

def merge_sort_helper(arr, low, high):
    if  low == high: return
    mid = (low + high) //2

    merge_sort_helper(arr,low,mid)
    merge_sort_helper(arr,mid+1,high)

    left = low
    right = mid+1
    merged = []
    while left < mid+1 and right < high+1:
        if arr[left] < arr[right]:
            merged.append(arr[left])
            left+=1
        else:
            merged.append(arr[right])
            right+=1

    while left <=mid:
        merged.append(arr[left])
        left+=1

    while right <=high:
        merged.append(arr[right])
        right+=1

    for i in range(low,high+1):
        print(arr, i,low,i-low)
        arr[i] = merged[i-low] #INSIGHT -> i- low will always ensure the you are taking from the zero'th index for the merged arr.
    

arr = [6,5,4,3,2,1]
merge_sort_helper(arr,0,len(arr)-1)   
print(arr)
