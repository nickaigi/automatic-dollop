def minesweeper(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        temp = []
        for j in range(cols):
            if matrix[i][j]:
                temp.append(1)
            else:
                temp.append(0)
        result.append(temp)
    return result
