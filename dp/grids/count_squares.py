# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# its just maximal squares in disguise

from typing import List
def countSquares(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0]*(cols+1) for _ in range(rows+1)]

    total =0
    for r in range(1,rows+1):
        for c in range(1, cols+1):
            if matrix[r-1][c-1] ==1:
                dp[r][c] = min(dp[r-1][c-1],dp[r-1][c],dp[r][c-1]) +1
                total+=dp[r][c]


    print(total)




countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]) #15
        