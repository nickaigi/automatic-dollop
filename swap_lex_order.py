def swap_lex_order(str_, pairs):
    d = {}
    d[str_] = True
    while True:
        old_len = len(d)
        for x, y in pairs:
            for s in list(d):
                d[swap(s, x, y)] = True
        if len(d) == old_len:
            return sorted(d)[-1]

def swap(str_, x, y):
    x = x - 1
    y = y - 1
    a = str_[x]
    b = str_[y]
    return str_[0:x] + b + str_[x + 1: y] + a + str_[y + 1:]

if __name__ == '__main__':
    str_ = 'abdc'
    pairs = [
        [1, 4],
        [3, 4],
    ]
    print(swap_lex_order(str_, pairs))
