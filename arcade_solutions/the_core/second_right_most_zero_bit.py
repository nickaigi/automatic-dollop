def second_right_most_zero_bit(n):
    return (((((n+1) | n) + 1) | n) -n)


if __name__ == '__main__':
    n = 37
    second_right_most_zero_bit(n)
