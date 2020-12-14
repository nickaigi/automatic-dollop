def neighbors(matrix,i,j,row,col):
    mine = 0
    if not ((i < 1) or (j < 1)):
        if matrix[i - 1][j - 1]:
            mine+=1
    if not (i < 1):
        if matrix[i - 1][j]:
            mine+=1
    if not ((i < 1) or (j >= col-1)):
        if matrix[i - 1][j + 1]:
            mine+=1
    if not (j >= col-1):
        if matrix[i][j + 1]:
            mine+=1
    if not ((i >= row-1) or (j >= col-1)):
        if matrix[i + 1][j + 1]:
            mine+=1
    if not (i >= row-1):
        if matrix[i + 1][j]:
            mine+=1
    if not ((i >= row-1) or (j < 1)):
        if matrix[i + 1][j - 1]:
            mine+=1
    if not (j < 1):
        if matrix[i][j - 1]:
            mine+=1
    return mine

def minesweeper(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(neighbors(matrix, i, j, rows, cols))
        result.append(temp)
    return result
