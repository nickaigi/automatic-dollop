def is_unstable_pair(a, b):
    return (a.upper() < b.upper()) != ( a < b)
