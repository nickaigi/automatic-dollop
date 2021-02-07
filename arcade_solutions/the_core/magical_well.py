def magical_well(a, b, n):
    bal = 0
    for i in range(n):
        bal += a * b
        a += 1
        b += 1
    return bal


if __name__ == '__main__':
    a = 1
    b = 2
    n = 2
    print(magical_well(a, b, n))
