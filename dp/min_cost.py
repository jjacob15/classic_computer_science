def min_cost(grid):
    rows,cols = len(grid), len(grid[0])
    
    dp = [[0]*(cols) for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            carry_forward = 0
            if r == 0 and c > 0:
                carry_forward = dp[r][c-1]
            elif r > 0 and c == 0:
                carry_forward = dp[r-1][c]
            else:
                carry_forward = min(dp[r-1][c], dp[r][c-1])

            dp[r][c] = grid[r][c] + carry_forward

    return dp[r][c]