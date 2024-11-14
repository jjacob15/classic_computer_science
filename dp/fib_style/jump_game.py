# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

#insight -> with each step, you reduce the last step and find max of current value and last step. keep the final step index to see if you reach the end.
def canJump(nums):
    n = len(nums)
    # if n == 1:
    #     return True
    dp = [1]+[0] * (n)
    final_step = 0
    for i in range(1, len(nums)+1):
        last_steps =dp[i-1]
        if last_steps > 0:
            dp[i] = max(last_steps-1,nums[i-1])
            final_step = i
    
    print(dp,final_step)
    if final_step == n:
        return True
    else:
        return False

# canJump([2,3,1,1,4]) #true
canJump([3,2,1,0,4]) #false
# canJump([2,0,0]) #true
# canJump([0]) #true