# Longest Sub-Array with Sum K
    
# Input: arr[] = [10, 5, 2, 7, 1, 9], k = 15
# Output: 4
# Explanation: The subarray [5, 2, 7, 1] has a sum of 15 and length 4.

#INSIGHT -> understand prefix sum. A prefix sum is the sum until the position i of an array [1,2,3,4] -> prefix sum of i 2 = 1+2+3 = 6. if you 
# hash every prefix sum, you can look back to find prefix sum - target in hash. if so current pos - hash position gives the array length

import sys
def longestSubarrayWithSumK(arr, target):
    hash = {}
    longest = -sys.maxsize
    prefix_sum = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == target: #regular check
            longest = max(longest, i+1)
        if prefix_sum - target in hash: #check if current prefix sum - target exists in hash then current pos - that pos gives you the arr length
            longest = max(longest, i - hash[prefix_sum - target])

        hash[prefix_sum] = i

    print(longest)

    

longestSubarrayWithSumK([1, 2,3,1,1,1],3) # 3
longestSubarrayWithSumK([-1, 2, -3],-2) # 3
longestSubarrayWithSumK([1, -1, 5, -2, 3],3) # 4