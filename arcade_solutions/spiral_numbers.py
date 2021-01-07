def spiral_numbers(n):
    matrix = []
    count = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(count)
            count += 1
        matrix.append(row)
    print(matrix)


if __name__ == '__main__':
    n = 3
    spiral_numbers(n)
