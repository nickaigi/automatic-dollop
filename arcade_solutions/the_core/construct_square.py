def construct_square(s):
    p = len(s)
    d_max = int((10**p)**.5)
    d_min = int((10**(p-1))**.5)

    for d in range(d_max, d_min -1, -1):
        n = str(d * d)
        if sorted(s.count(c) for c in set(s)) == sorted(n.count(c) for c in set(n)):
            return int(n)
    return -1


if __name__ == '__main__':
    s = 'ab'
    print(construct_square(s))
