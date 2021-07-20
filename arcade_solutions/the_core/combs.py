def check_for_carry(a1, a2):
    res = []
    for x, y in zip(a1, a2):
        if x == 1 and y == 1:
            # carry
            pass
        else:
            pass
    return res


def gen_array(s):
    return [1 if c == '*' else 0 for c in s]


def combs(c1, c2):
    c1 = gen_array(c1)
    c2 = gen_array(c2)
    for x, y in zip(c1, c2):
        print(x, y)
    return 0


if __name__ == '__main__':
    c1 = '*..*'
    c2 = '*.*'
    print(combs(c1, c2))
