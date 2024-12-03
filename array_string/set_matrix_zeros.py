# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
#INSIGHT-> using hash to keep the rows and cols to zero out.
#INSIGHT -> for space of O(1), have a boolean if first row and col needs to be zero, then for row and col1 , update the marker on row and col zero.
#use that to zero the array.
def setZeroes_lowspace(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    firstRowZero = any(matrix[0][c] == 0 for c in range(cols))
    firstColZero = any(matrix[r][0] == 0 for r in range(rows))

    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 1
                matrix[0][c] = 1
    # print(zeroRows,zeroCols)
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[r][0] == 0 or matrix[0][c] ==0:
                matrix[r][c] = 0

    if firstRowZero:
        for c in range(cols):
            matrix[0][c] = 0

    if firstColZero:
        for r in range(rows):
            matrix[r][0] = 0
    print(matrix)

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    zeroRows = {}
    zeroCols = {}
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zeroRows[r] = 1
                zeroCols[c] = 1
    # print(zeroRows,zeroCols)
    for r in range(rows):
        for c in range(cols):
            if r in zeroRows or c in zeroCols:
                matrix[r][c] = 0
    print(matrix)
    




setZeroes_lowspace([[0,1,2,0],[3,4,5,2],[1,3,1,5]])