# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#INSIGHT -> lets say you are placing a queen at 0,0, feasibility is validated if any queen exists diagonally top left, left or diagonoally bottom left
#INSIGHT -> when you place a queen on 0,0 you then go through each row and check if feasible, then incement col. If not, backtrack and clear that position.

def totalNQueens(n):

    def isFeasible(row,col,board):
        # 
        rowCopy = row
        colCopy = col

        #Looking at the top left diagonal
        while row>=0 and col >=0:
            if board[row][col] == "Q":
                return False
            row -=1
            col -=1

        row = rowCopy
        col = colCopy
        #Looking at the left
        while col >=0:
            if board[row][col] == "Q":
                return False
            col -=1

        row = rowCopy
        col = colCopy
        #Looking at bottom left diagonal
        while row <n and col>=0:
            if board[row][col] == "Q":
                return False
            row +=1
            col -=1

        return True
    
    def search(col, board, ans, n):
        if col == n:
            ans.append([row[:] for row in board])
            return
        
        for row in range(n):
            if isFeasible(row,col,board):
                board[row][col] = "Q"
                search(col+1, board, ans, n)
                board[row][col] = "."


    ans = []
    board = [["."]*n for _ in range(n)]
    search(0,board,ans,n)
    print(ans)

totalNQueens(4) #2