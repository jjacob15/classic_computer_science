# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 


def jump(nums):
    n = len(nums)
    if n <= 1:
        return 0
    dp = [float('inf')] * n  # Initialize the dp array with infinity
    dp[0] = 0  # It takes 0 jumps to reach the starting position

    for i in range(1,n):
        for j in range(i):
            print(i,j,nums[j])
            if j + nums[j] >= i:  # If position j can reach position i
                print(i,j,nums[j],dp[j])
                dp[i] = min(dp[i], dp[j] + 1)  # Take the minimum jumps to reach i
                print(dp)


# jump([2,3,1,1,4]) #2
# jump([2,3,0,1,4]) #2
# jump([2,1,1,1,1]) #3
jump([4,1,1,1,1,1,1]) #3
# jump([0]) #0