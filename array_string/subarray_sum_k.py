# Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# INSIGHT -> [1,2,3,4] ,[1] ,[1,2] ,[2,3,4] [4] are all SUBARRAYS. [1,3] is a SUBSEQUENCE
# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

#INSIGHT -> understand prefix_sum in the longest_subarray_sum_k problem

def subarraySum(nums, k):
    prefix_sum = 0
    hash = {}
    count =0 
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum == k:
            count+=1
        if prefix_sum - k in hash:
            count += hash[prefix_sum - k]
        
        if prefix_sum in hash:
            hash[prefix_sum]+=1
        else:
            hash[prefix_sum]=1

    return count


subarraySum([1,1,1],2) # 2
subarraySum([1,2,3],3) # 2