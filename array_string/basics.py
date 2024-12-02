def largest(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    
def left_rotate_arr(arr):
    def reverse(arr,start,end):
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start+=1
            end-=1

    reverse(arr,0,len(arr)-1)
    reverse(arr,0,len(arr)-2)

#INSIGHT -> k times, you find remainder of the number of times with the len. to restrict the times to len of arr
#Moudulus for anything within a bound
def rotate_arr_k(arr,k):
    steps = k%len(arr)
    def reverse(arr,start,end):
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start+=1
            end-=1

    reverse(arr,0,len(arr)-1)
    reverse(arr,0,steps-1)
    reverse(arr,steps,len(arr)-1)

# rotate_arr_k([1,2,3,4,5,6,7],2)

#INSIGHT-> don't think of ==0 think !=0 to move all zeros to the end. 
def remove_zeros(arr):
    i = j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j],arr[i] = arr[i],arr[j]
            j+=1
    print(arr)
# remove_zeros([1,0,2,3,0,4,0,1])

#find the longest subarray for the target
#INSIGHT -> subarrays are usually two pointers as they only look forward usinge very element
def longest_subarray_with_sum(arr,target):
    j = 0
    max_subarray = 0
    for i in range(len(arr)):
        k = target - arr[i]
        count = 1
        j= i+1
        while j < len(arr) and k > 0:
            k = k - arr[j]
            count+=1
            j+=1
        if k == 0:  
            max_subarray = max(max_subarray,count)
    print(max_subarray)
# longest_subarray_with_sum([2,3,5,1,9],10)

def longest_subarray_with_sum_with_neg(arr,target):
    j = 0
    max_subarray = 0
    for i in range(len(arr)):
        k = target - arr[i]
        count = 1
        j= i+1
        while j < len(arr):
            k = k - arr[j]
            count+=1
            j+=1
        if k == 0:  
            max_subarray = max(max_subarray,count)
    print(max_subarray)
longest_subarray_with_sum_with_neg([-1,1,1],1)
