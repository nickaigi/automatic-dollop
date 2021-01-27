def second_right_most_zero_bit(n):
    return (n | (n+1) + 1) & ~(n | (n+1))


if __name__ == '__main__':
    n = 37
    second_right_most_zero_bit(n)
