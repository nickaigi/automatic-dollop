def kill_kth_bit(n, k):
    """
    use bitwise AND
        0 & 0 = 0
        1 & 0 = 0

    to clear the bit: perform a bitwise AND of the number with a reset bit
    n = n & ~(1 << k)

    OR

    n &= ~(1 << k)
    """
    return n & ~(1 << k - 1)


if __name__ == '__main__':
    n = 37
    k = 3
    print(kill_kth_bit(n, k))
