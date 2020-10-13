def get_tiny(a, b, k):
    tiny = []
    b.reverse()
    for i, j in list(zip(a, b)):
        x = (10 * i) + j
        if x < k:
            tiny.append(x)
    return len(tiny)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [4, 5, 6]
    k = 50

    print(get_tiny(a, b, k))
