def equal_pair_of_bits(n, m):
    return ~(n ^ m) & ((n ^ m) + 1)
