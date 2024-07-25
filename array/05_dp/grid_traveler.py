def grid_traveler(row,col):
    grid = [[0 for i in range(row+2)] for j in range(col+2)]
    
    grid[1][1] = 1
    
    for c in range(col+1):
        for r in range(row+1):
            grid[c+1][r] += grid[c][r]
            grid[c][r+1] += grid[c][r]

    return grid[3][3]

