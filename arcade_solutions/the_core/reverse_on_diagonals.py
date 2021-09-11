def reverse_on_diagonals(m):
    for i in range(len(m) // 2):
        m[i][i], m[-i-1][-i-1] = m[-i-1][-i-1], m[i][i]
        m[i][-i-1], m[-i-1][i] = m[-i-1][i], m[i][-i-1]
    return m


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(reverse_on_diagonals(matrix))
