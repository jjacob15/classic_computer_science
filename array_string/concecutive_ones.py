# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 
def findMaxConsecutiveOnes(nums):
    max_count = 0
    current = 0
    for i in nums: #INSIGHt -> don't use range.
        if i == 1:
            current+=1
            if current > max_count:  # don't use max instead use greater check
                max_count = current
        else:
            current = 0
    return max_count