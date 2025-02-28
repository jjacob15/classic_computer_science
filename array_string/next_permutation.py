# Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the
#  array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows
#  it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

#INSIGHt -> go from end, until you find i > i -1. Swap, then sort the remaining.
#INSIGHT => if you are using a for and if for something, use a while.

# -> 4325431
# 43(2)5431  first decreasing element from the right. If no element is found, its the last permutation, reverse and return
# 43(2)54(3)1 find next largest element from tail. the first hit.
# 43(3)54(2)1 swap
# 433(1245)reverse not sort 

def nextPermutation(nums):
    l = len(nums) -1

    # Step 1: Find the first decreasing element (from the right)
    while l > 0 and nums[l-1] > nums[l]:
        l = l-1

    if l == 0:
         # If no such element is found, it's the last permutation, reverse to the first
        nums.reverse()
        print(nums)
        return
    start = l - 1

    # Step 2: Find the smallest element larger than nums[start] to swap with
    l = len(nums) -1
    while nums[l] <= nums[start]:
        l=l-1
    swap_pos = l
     
     # Step 3: Swap
    nums[start],nums[swap_pos]  = nums[swap_pos], nums[start]
    
    # Step 4: Reverse the suffix (right portion)
    nums[start+1:] = reversed(nums[start+1:])
    print(nums)




nextPermutation([3,2,1]) # 123
nextPermutation([1,2,3]) # 132
nextPermutation([1,1,5]) # 151
nextPermutation([1,3,2]) # 213
nextPermutation([2,3,1]) # 312
nextPermutation([4,3,2,5,4,1,3]) #4323125
nextPermutation([4,3,2,5,4,3,1]) #4331245
