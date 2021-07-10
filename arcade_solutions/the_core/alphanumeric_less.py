def tokenize(s):
    tokens = []
    for c in s:
        pass
    return tokens


def alphanumeric_less(s1, s2):
    t1 = tokenize(s1)
    t2 = tokenize(s2)

    for x, y in zip(t1, t2):
        pass
    return False



if __name__ == '__main__':
    s1 = 'a'
    s2 = 'a1'
    print(alphanumeric_less(s1, s2))
