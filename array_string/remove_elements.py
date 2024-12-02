# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# simple 2 pointer
def removeElements(nums,val):
    s = w = 0
    while s < len(nums):
        if nums[s] != val:
            nums[w] = nums[s]
            w+=1
        s+=1

    print(nums)

    # temp=fast = 0
    # while fast < len(nums):
    #     if nums[fast] == val:
    #         temp = fast
    #         while fast < len(nums) and nums[fast] == val:
    #             fast+=1
    #         if fast == len(nums): break
    #         nums[temp],nums[fast] = nums[fast],nums[temp]
    #         fast=temp
    #     else:
    #         fast+=1
        
    # count = 0
    # for i in nums:
    #     if i != val:
    #         count+=1
    # return count


removeElements([0,1,2,2,3,0,4,2],2)
