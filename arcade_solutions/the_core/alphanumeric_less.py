def tokenize(s):
    return [c for c in s]


def alphanumeric_less(s1, s2):
    t1 = tokenize(s1)
    t2 = tokenize(s2)
    print(t1, t2)

    for x, y in zip(t1, t2):
        if x != y:
            return False
    return True



if __name__ == '__main__':
    s1 = 'a'
    s2 = 'a1'
    print(alphanumeric_less(s1, s2))
