def all_longest_strings_old(st):
    l = max([len(s) for s in st])
    return [s for s in st if len(s) == l]


def all_longest_strings(st):
    return [s for s in st if len(s) == max(map(len, s))]
