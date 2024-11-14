#INSIGHT ->  top + left = new ways to get to current position. To do that, either initialize first row and col to 1 or have just first cell as 
# 1 and look back. grid[r-1][c] +=grid[r][c] and grid[r][c-1] += grid[r][c]

def grid_traveler(row,col):
    grid = [[0 for i in range(row+1)] for j in range(col+1)]
    
    for i in range(row+1):
        grid[i][0] = 1
        
    for j in range(col+1):
        grid[0][j] = 1

    print(grid)
    
    for c in range(1,col):
        for r in range(1,row):
            grid[r][c] = grid[r-1][c]+ grid[r][c-1]

    print(grid)
    return grid[3][3]


grid_traveler(3,3)


