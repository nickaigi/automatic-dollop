def reverse_on_diagonals(matrix):
    forward_counter = 0
    reverse_counter = len(matrix) - 1 
    first_diagonal = []
    second_diagonal = []
    for row in matrix:
        first_diagonal.append(row[forward_counter])
        second_diagonal.append(row[reverse_counter])
        forward_counter += 1
        reverse_counter -= 1
    return first_diagonal, second_diagonal


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(reverse_on_diagonals(matrix))
