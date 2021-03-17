def strings_construction(a, b):
    return min(b.count(c) // a.count(c) for c in a)

def strings_construction_long(a, b):
    c = set()
    for x in set(a):
        c.add(b.count(x) // a.count(x))
    return min(c)
