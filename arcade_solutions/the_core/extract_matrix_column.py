def extract_matrix_column(m, c):
    return [x[c] for x in m]


if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 2],
        [0, 5, 0, 4],
        [2, 1, 3, 6]
    ]
    column = 2
    print(extract_matrix_column(matrix, column))
