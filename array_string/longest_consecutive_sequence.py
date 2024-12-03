# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def lcs(arr):
    hash = {}
    max_val = 0
    for num in arr:
        hash[num] = 1
    for num in arr:
        if num - 1 not in hash: # INSIGHT-> this is what makes its O(N) instead of O(N^2). because it does not check the values 4,3,2 in the first array but just 1
            cnt = 1
            x = num
            while x+1 in hash:
                cnt+=1
                x+=1
            max_val = max(max_val,cnt)
    print(max_val)
    return max_val

lcs( [100,4,200,1,3,2])
lcs( [0,3,7,2,5,8,4,6,0,1])
