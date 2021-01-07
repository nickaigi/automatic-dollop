def spiral_numbers(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    print(matrix)


if __name__ == '__main__':
    n = 3
    spiral_numbers(n)
