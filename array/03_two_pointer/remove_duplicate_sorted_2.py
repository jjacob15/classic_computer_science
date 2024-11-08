# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#Here index only copies if the occurance is under 2 else it ignores
from collections import Counter
def remove_duplicate(nums):
    index = 1
    occurance =1

    for i in range(1, len(nums)):
        if nums[i]== nums[i-1]:
            occurance+=1
        else:
            occurance = 1
        
        if occurance <=2:
            nums[index] = nums[i]
            index+=1
    print(nums,index)


remove_duplicate([0, 0,1,1,1,1,2,3,3])
remove_duplicate([1,1,1,2,2,3])