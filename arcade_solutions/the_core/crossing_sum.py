def crossing_sum(m, a, b):
    return sum(m[a]) + sum([i[b] for i in m]) - m[a][b]


if __name__ == '__main__':
    m = [
        [1, 1, 1, 1], 
        [2, 2, 2, 2], 
        [3, 3, 3, 3]
    ]
    a = 1
    b = 3
    print(crossing_sum(m, a, b))
