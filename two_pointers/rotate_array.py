# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# INSIGHT-> k is not the index, its the number of times the rotation happens. It can't go beyond the len of the array, so you use mod for that

def rotate(nums, k) -> None:
    n = len(nums)
    k %=n # this is to bound the rotations within limit of the array
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