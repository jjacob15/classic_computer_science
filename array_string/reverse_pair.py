# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

def reverse_pair(arr):
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
                i +=1
            while j < len(right):
                arr[k] = right[j]
                k+=1
                j +=1

            i, j =0,0
            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    count += mid - i 
                    j+=1
                else:
                    i+=1

    merge_sort(arr)
    return count


print(reverse_pair([1,3,2,3,1]) == 2)
print(reverse_pair([2,4,3,5,1]) == 3)