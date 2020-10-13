def matrixElementsSum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    cost = 0
    for i in range(rows):
        for j in range(cols):
            current_value = matrix[i][j]  
            if i == 0:
                cost += matrix[i][j]
            else:
                if matrix[(i-1)][j] != 0 and matrix[0][j] !=0:
                    cost += matrix[i][j]
    return cost


if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 2],
        [0, 5, 0, 0],
        [2, 0, 3, 3],
    ]
    matrix_two = [
        [1, 1, 1, 0],
        [0, 5, 0, 1],
        [2, 1, 3, 10],
    ]
    print(matrixElementsSum(matrix))
    print(matrixElementsSum(matrix_two))
