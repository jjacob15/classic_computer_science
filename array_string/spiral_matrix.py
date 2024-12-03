#this is the case of looking for each bound and working through it .
def spiralOrder(matrix):
    r = len(matrix) -1
    c = len(matrix[0]) -1

    cr = 0
    cc = 0
    visited = {}
    result = []

    if r == 0:
        return matrix[0]
    if c == 0:
        return[matrix[i][0] for i in range(len(matrix))]
    if c ==0 and  r ==0:
        return matrix   

    while (cr,cc) not in visited:
        while cr >= 0 and cc <= c and (cr,cc) not in visited:
            visited[(cr,cc)] = 1
            result.append(matrix[cr][cc])
            cc+=1
        cc -=1
        cr +=1
        while cc >= 0 and cr <= r and (cr,cc) not in visited:
            visited[(cr,cc)] = 1
            result.append(matrix[cr][cc])
            cr+=1
        cc -=1
        cr -=1        
        while cc >= 0 and (cr,cc) not in visited:
            result.append(matrix[cr][cc])
            visited[(cr,cc)] = 1
            cc -= 1
        cc+=1
        cr-=1    
        while cr >= 0 and (cr,cc) not in visited:
            result.append(matrix[cr][cc])
            visited[(cr,cc)] = 1
            cr -= 1           
        cr +=1
        cc +=1
    print(result)
    return result
    
# spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
# spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,6,9,8,7,4,5]
# spiralOrder([[1]]) == [1]
spiralOrder([[3],[2]]) == [1]