def minesweeper(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j])
