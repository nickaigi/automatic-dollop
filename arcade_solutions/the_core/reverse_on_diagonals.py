def reverse_on_diagonals(matrix):
    size = len(matrix) - 1

    first_diag = []
    second_diag = []

    for i in range(len(matrix)):
        first_diag.append(matrix[i][i])
        second_diag.append(matrix[i][size])
        size -= 1
    return first_diag, second_diag

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(reverse_on_diagonals(matrix))
