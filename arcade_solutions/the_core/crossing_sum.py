def crossing_sum(m, a, b):
    row = [i for i in m[a]]
    col = [m[i][b] for i in range(len(m)) if i != a]
    return sum(row) + sum(col)


if __name__ == '__main__':
    m = [
        [1, 1, 1, 1], 
        [2, 2, 2, 2], 
        [3, 3, 3, 3]
    ]
    a = 1
    b = 3
    print(crossing_sum(m, a, b))
