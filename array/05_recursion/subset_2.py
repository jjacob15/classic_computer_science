# find all the subsets

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Skipping ensures each subset is generated only once, even if duplicates are present in the input. By not revisiting the second instance of each duplicate

from typing import List
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() #sort so skipping adjacent values work
        def backtrack(start, combination):
                result.append(combination[:])
                if start == len(nums):
                       return 

                for end in range(start,len(nums)):
                    if end > start and nums[end] == nums[end-1]:
                           continue
                    combination.append(nums[end])
                    backtrack(end+1,combination)
                    combination.pop()

        backtrack(0,[])
        print(result)


subsetsWithDup([1,2,2])