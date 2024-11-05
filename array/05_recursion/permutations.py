# Permutations
# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order.
#INSIGHT-> when you are doing permutations, don't use an index, you need all of it.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

def permute(arr):
    result = []


    def backtrack(combinations):
        if len(combinations) == len(arr):
            result.append(combinations[:])
            return
        
        for val in arr:
            if val in combinations: continue
            combinations.append(val)
            backtrack(combinations)
            combinations.pop()

    backtrack([])
    print(result)

permute([1,2,3])    