# find the subset of non adjacent with the maximum sum
# arr = [-2,1,3,-4,5]

#INSIGHT -> DP, start from the 2n position and use max of either the pervious or arr[i] + dp[i-2]. 
# This is because the max should only be the previous value or current + dp[i-2] which will take care of teh adjacancy requirement

def max_arr_sum(arr):
    # dp = [0]*len(arr)
    # dp[0] = arr[0]
    # dp[1] = arr[1]

    # max_sum =0
    # print(dp)
    # for outer in range(len(arr)):
    #     for inner in range(outer+2,len(arr),1):
    #         dp[inner] = max(arr[inner], dp[inner - 2] + arr[inner])
    #         print(dp)
    #         max_sum = max(max_sum,dp[inner])
    
    # print(dp)
    # return max_sum
    if not arr:
        return 0
    n = len(arr)
    if n == 1:
        return max(0, arr[0])
    
    dp = [0] * n
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
    return dp[-1]    