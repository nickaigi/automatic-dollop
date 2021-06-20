def all_longest_strings(st):
    l = max([len(s) for s in st])
    return [s for s in st if len(s) == l]
