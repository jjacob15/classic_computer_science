#INSIGHTS -> as it satisfies two conditions for DP, we choose dp. Its a  min/max problem and future decision depends of previous.
#INSIGHT -> don't worry about future, i.e n+1. only look at the past.

# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element   
# equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.

# INSIGHT ->
# If each DP state represents a choice for each element position in nums, then the DP array typically has a length equal to
#  nums (e.g., len(nums)).
# If each DP state represents a decision based on the values themselves (like earning points based on the value of i), 
# then the DP array is usually based on the maximum number in nums (max(nums) + 1).



from collections import defaultdict
def deleteAndEarn(nums):
    dict = defaultdict(int)
    max_val = 0
    for num in nums:
        dict[num] += num
        max_val = max(num,max_val)

    dp = [0] * (max_val+1) # for zero the max profit is zero,
    dp[1] = dict[1] # for one the max profit is the count of 1 in the  past. for two, we either take gain of 2 + max at 0 or max at 1.

    for k in range(2, len(dp)):
        gain = dict[k]
        max_if_taken = gain + dp[k-2]
        max_if_not_taken = dp[k-1]
        print(k, "->", gain, "take->", max_if_taken, "don't take->", max_if_not_taken)
        dp[k] = max(max_if_not_taken,max_if_taken)

    print(dp)
    return max(dp)





# deleteAndEarn([3,4,2])
# deleteAndEarn([2,2,3,3,3,4])
deleteAndEarn([1,1,1,2,4,5,5,5,6])