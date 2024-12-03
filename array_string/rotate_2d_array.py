#rotate nxm array.
#INSIGHT -> you do it by first transposing the matrix. i.e. i,j becomes j,i. Then reverse each row.
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i,n): # to transpose, like in excel, start with i to keep it below diagonal
            print(i,j)
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    print(matrix)
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    print(matrix)

rotate([[1,2,3],[4,5,6],[7,8,9]])