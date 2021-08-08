def swap_diagonals(m):
    for i in range(len(m)):
        m[i][i], m[i][-i-1] = m[i][-i-1], m[i][i]
    return m


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(swap_diagonals(matrix))
