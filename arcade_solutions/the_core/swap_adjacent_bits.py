def swap_adjacent_bits(n):
    return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)


if __name__ == '__main__':
    n = 13
    swap_adjacent_bits(n)
