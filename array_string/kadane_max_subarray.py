#kadanes algo to find max subarray
#when the accumlated value go under 1, reset to current idx and number. to fix the max array, just use temp idx and 
def max_subarray_sum_db(nums):
    max_val = nums[0]
    current_sum =  temp_start = 0
    start = end =0
    for i, num in enumerate(nums):
        if current_sum <= 0:
            temp_start = i
            current_sum = num
        else:
            current_sum += num
        
        if current_sum > max_val:
            max_val = current_sum
            start, end = temp_start, i
    return max_val, arr[start:end+1]

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, max_subarray = max_subarray_sum_db(arr)
print("Max Sum:", max_sum)
print("Max Subarray:", max_subarray)



















    # sub_array = nums[0]
    # max_val  = nums[0]
    # for i in range(1,len(nums)):
    #     sub_array = max(nums[i], sub_array + nums[i])
    #     max_val  = max(max_val,sub_array)
