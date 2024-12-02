#kadanes algo to find max subarray, All you are doing is checking if max(num[i] ,curr_sum + num[i])
# add it to the maxvalue
#INSIGHT-> its a DP problem. Checking if the last subarray + current value is > that current value then use the sum else just use current value.
import sys
def max_subarray_sum_db(nums):
    sub_array = nums[0]
    max_val  = nums[0]
    for i in range(1,len(nums)):
        sub_array = max(nums[i], sub_array + nums[i])
        max_val  = max(max_val,sub_array)

    return max_val

