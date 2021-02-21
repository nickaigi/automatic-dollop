def gcd(a, b):
    while b:
         a, b = b, a % b
    return a


def count_black_cells(n, m):
    return n + m + gcd(n, m) - 2
