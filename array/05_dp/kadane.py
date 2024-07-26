#kadanes algo to find max subarray, All you are doing is checking if max(num[i] ,curr_sum + num[i])
# add it to the maxvalue

def max_subarray_sum(nums):
    curr_sum = nums[0]
    max_val  = nums[0]
    for i in range(1,len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_val  = max(max_val,curr_sum)

    return max_val
 