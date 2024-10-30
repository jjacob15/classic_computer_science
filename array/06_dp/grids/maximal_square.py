# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#INSIGHT -> creating a extra row and column helps with computing the first row and column values. 
# we are looking for a square with all ones, what we do is we look at the min of all four positions and add 1 to it. 
# # That will give you the dim of that square. finally we take the max and square it 

# ["1","0","1","0","0"]
# ["1","0","1","1","1"]
# ["1","1","1","1","1"]
# ["1","0","0","1","0"]

# this will give 

# [0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 0]
# [0, 1, 1, 2, 2, 1]
# [0, 1, 2, 2, 2, 1]
# [0, 1, 0, 0, 1, 0]

def max_square(matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        maxsqlen = 0
        # for convenience, we add an extra all zero column and row
        # outside of the actual dp table, to simpify the transition
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = (min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])+ 1)
                    maxsqlen = max(maxsqlen, dp[i][j])

        for row in matrix:
             print(row)
        print("-------------------------")
        for row in dp:
             print(row)
        print(maxsqlen * maxsqlen)
        return maxsqlen * maxsqlen

max_square([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]) #16
# max_square([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) #4
# max_square([["0","1"],["1","0"]]) #1
# max_square([["0","1"]]) #1
# max_square([["0","0"]]) #0
