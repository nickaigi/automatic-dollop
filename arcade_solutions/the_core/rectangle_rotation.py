import math


def rectangle_rotation(a, b):
    [m, n] = [int(math.floor(x / math.sqrt(2))) for x in (a, b)]
    return m * n + (m + 1) * (n + 1) - (m + n) % 2
