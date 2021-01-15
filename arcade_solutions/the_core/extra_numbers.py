def extra_numbers(a, b, c):
    if a == b:
        return c
    if a == c:
        return b
    return a


def extra_numbers_short(a, b, c):
    """
    using the bitwise exclusive Or
    a ^ b == xor(a, b)
    """
    return a ^ b ^ c
