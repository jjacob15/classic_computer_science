# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
def totalNQueens(n):

    def isFeasible(positions,cellrow,cellcol):
        for r,c in positions:
            if r == cellrow or c == cellcol:
                return False
            diagRow = r
            diagCol = c
            if diagRow !=0 and diagCol !=0:
                diagCol = n -1 - r
                diagRow = n -1 - c
            increment = 0
            while increment < n:
                if diagRow >=n or diagCol >= n:
                    return True
                if cellrow == diagRow and cellcol == diagCol:
                    return False
                diagRow+=1
                diagCol+=1

        
        return True


    def search(positions,cellrow,cellcol):
        if len(positions) == n:
            print(positions)
            return True
        
        if cellrow <0 or cellrow >= n or cellcol <0 or cellcol >=n:
            print("here")
            return False
        
        if not isFeasible(positions,cellrow,cellcol):
            positions.clear()
            return False
        else:
            print("s here")
            positions.append([cellrow,cellcol])

        
        for searchRow in range(0,n):
            for searchCol in range(0,n):
                found = (search(positions,searchRow+1,searchCol) or
                        search(positions,searchRow-1,searchCol) or
                        search(positions,searchRow,searchCol+1) or
                        search(positions,searchRow,searchCol-1))
            
                print(found,searchRow,searchCol)

    search([],0,0)
    # print(isFeasible([[2,0]],2,2))
    # print(isFeasible([[1,3]],2,2))
    # print(isFeasible([[3,3]],2,2))
    # print(isFeasible([[3,1]],2,2))


totalNQueens(4) #2