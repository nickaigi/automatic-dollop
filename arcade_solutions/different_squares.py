def different_squares(matrix):
    s = set()

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            two_by_two = (
                matrix[i][j], matrix[i][j+1], matrix[i + 1][j], matrix[i+1][j+1]
            )
            s.add(two_by_two)
    return len(s)
                


if __name__ == '__main__':
    matrix = [
        [1, 2, 1],
        [2, 2, 2],
        [2, 2, 2],
        [1, 2, 3],
        [2, 2, 1],
    ]

    print(different_squares(matrix))
