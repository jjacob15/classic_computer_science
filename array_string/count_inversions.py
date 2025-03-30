# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

def count_inversions(arr):
    count = 0
    def merge_sort(arr):
        nonlocal count
        n = len(arr)
        if n > 1:
            mid = n//2
            left = arr[:mid]
            right = arr[mid:]

            merge_sort(left)
            merge_sort(right)

            i = 0 
            j = 0
            k = 0
            print("lr",left,right,mid)
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    k+=1
                    i+=1
                else:
                    arr[k] = right[j]
                    k+=1
                    j+=1
                    count +=(mid - i)
                    print("adding",i,j,(mid - i))

            while i < len(left):
                arr[k] = left[i]
                k+=1
                i +=1
            while j < len(right):
                arr[k] = right[j]
                k+=1
                j +=1

    merge_sort(arr)
    print(count)
    return count


print(count_inversions([5,3,2,4,1]) == 8)