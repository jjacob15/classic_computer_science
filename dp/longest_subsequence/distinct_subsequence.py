# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

# "abc" and "" then return 1. If there is 

 
def numDistinct(s,t):
    m, n = len(s), len(t)
    
    # Initialize the dp table with (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: An empty t can be formed by any prefix of s by deleting all characters
    for i in range(m + 1):
        dp[i][0] = 1
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    # The result is the number of distinct subsequences of t in s
    for row in dp:
        print(row)
    print(dp[m][n])
    return dp[m][n]

numDistinct("rabbbit","rabbit") #3
# numDistinct("babgbag","bag") #3
# numDistinct("aaba","a") #3
