def different_squares(matrix):
    digits = [x for sublist in matrix for x in sublist]
    digits_set = set(digits)
    if len(digits_set) == 1:
        return 1
    print(digits_set)


if __name__ == '__main__':
    matrix = [
        [1, 2, 1],
        [2, 2, 2],
        [2, 2, 2],
        [1, 2, 3],
        [2, 2, 1],
    ]

    different_squares(matrix)
