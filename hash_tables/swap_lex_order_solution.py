def swapLexOrder(str_, pairs):
    if not str_ or not pairs:
        return ('', str_)[not pairs]

    list_ = [''] + list(str_)
    setted_pairs = list(map(set, pairs))
    while setted_pairs:
        path = setted_pairs.pop(0)
        while True:
            path_one = path.copy()
            for pair in setted_pairs:
                if path_one & pair:
                    path |= pair
                    setted_pairs.remove(pair)
            if path == path_one:
                break
        optimal = sorted(list_[i] for i in path)
        for i, v in enumerate(sorted(path, reverse=True)):
            list_[v] = optimal[i]
    return ''.join(list_[1:])
