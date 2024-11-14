# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 
def exits(board,word):
    rows,cols = len(board),  len(board[0])
    wl = len(word)

    positions = []
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                positions.append([r,c])

    found = False
    def backtrack(word_idx, r,c):
        if word_idx == wl:
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or word_idx >= wl or word[word_idx] != board[r][c]:
            return False
        
        temp, board[r][c] = board[r][c], '#'
        found =  (backtrack(word_idx+1,r,c+1) or 
        backtrack(word_idx+1,r,c-1) or
        backtrack(word_idx+1,r+1,c) or
        backtrack(word_idx+1,r-1,c))
        board[r][c] = temp
        return found



    for r,c in positions:
        if backtrack(0,r,c):
            return True
        
    return False




exits([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")