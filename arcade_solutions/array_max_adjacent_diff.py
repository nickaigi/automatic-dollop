# array maximal adjacent difference
def array_max_adjacent_diff(a):
    diff = []
    for x, y in zip(a[:-1], a[1:]):
        diff.append(abs(x - y))


if __name__ == '__main__':
    a = [2, 4, 1, 0]
    print(array_max_adjacent_diff(a))
