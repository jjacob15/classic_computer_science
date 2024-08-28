# You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the
#  edge of the grid or a blocked cell. Given a grid, a start and a goal, determine the minmum number of moves to get to the goal.

# ...
# .X.
# ...

# start = (0,0)
# goal = (1,2)
# (0, 0) -> (0,2) -> (1,2) = 2 moves

# INSIGHT -> we preset directsion so x -1 is up x+1 is down and so on for y. Visiting is important to avoid repeating searched path.
# INSIGHT -> In this problem you had to go to the end of the edge, so we are using while loop to do it.

def castle_on_the_grid(grid, startX, startY, goalX, goalY):
    n = len(grid)
    queue = []

    directions = [(-1,0),(1,0),(0,-1),(0,1)] #up, down, left,right
    visited = [[False] * (n) for _ in range(n)]
    visited[startX][startY] = True
    queue.append((startX, startY, 0))  # the last the move count

    while queue:
        x,y, moves = queue.pop(0)

        if x == goalX and y == goalY:
            return moves
        
        for dx,dy in directions:
            nx,ny = x,y
            while 0 <= nx +dx < n and 0<=ny+dy <n and grid[nx+dx][ny+dy] == ".":
                nx+=dx
                ny+=dy
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,moves +1))
    return -1