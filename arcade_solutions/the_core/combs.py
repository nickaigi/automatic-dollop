def mask(s):
    res  = 0
    for c in s:
        digit = 1 if c == '*' else 0
        res = (res << 1) + digit
    return res


def combs(c1, c2):
    l1 = len(c1)
    l2 = len(c2)

    res = l1 + l2

    m1 = mask(c1)
    m2 = mask(c2)

    for i in range(l1):
        if m2 << i & m1 == 0:
            tmp = max(l2 + i, l1)
            res = min(res, tmp)

    for i in range(l2):
        if m1 << i & m2 == 0:
            tmp = max(l1 + i, l2)
            res = min(res, tmp)

    return res


if __name__ == '__main__':
    c1 = '*..*'
    c2 = '*.*'
    print(combs(c1, c2))
