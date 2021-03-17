def strings_construction(a, b):
    return min(b.count(c) // a.count(c) for c in a)
