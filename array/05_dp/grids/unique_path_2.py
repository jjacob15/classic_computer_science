# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
#  bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
# Input: m = 3, n = 7
# Output: 28

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# INSIGHT  ->  here remember you are computing the forward possibililtes. 


def uniquePath2(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    dp[0][0] = 1
    for row in dp:
        print(row)

    print("----------------")
    for r in range(m):
        for c in range(n):
            if grid[r][c]!=1:
                dp[r+1][c] += dp[r][c]
                dp[r][c+1] += dp[r][c]


    for row in dp:
        print(row)

uniquePath2([[0,0,0],[0,1,0],[0,0,0]]) #2
# uniquePath(3,3) #3
# uniquePath(3,7) #28