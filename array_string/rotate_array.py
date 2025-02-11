# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    k %=n #INSIGHT -> this bounds the operations/steps within the array
    if n == 1:
        return nums
    if k >n:
        return nums
    
    def reverse(nums,i,j):
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1

    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    

rotate([1,2,3,4,5,6,7], 8)    
 
