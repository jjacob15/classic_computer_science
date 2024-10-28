# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).
# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
# Return the knight's minimum initial health so that he can rescue the princess.
# Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7
# Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

#HARD.
from typing import List
def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    m, n = len(dungeon), len(dungeon[0])
    
    # Initialize dp array with infinity
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    
    # Bottom-right corner setup (destination)
    dp[m][n-1] = dp[m-1][n] = 1
    for row in dp:
        print(row)
    
    # Populate the dp table from bottom-right to top-left
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            min_hp_needed = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = max(1, min_hp_needed)
    
    # The minimum initial health required at the start
    for row in dp:
        print(row)
    return dp[0][0]


    


calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]) #7
calculateMinimumHP([[-3,5]]) #4
