# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

def tribonacci(n):

    dp = [0]*(n+1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    return dp[-1]


tribonacci(25)==4