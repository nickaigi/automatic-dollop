def different_right_most_bit(n, m):
    return (n ^ m) & -(n ^ m)


if __name__ == '__main__':
    n = 11
    m = 13
    print(different_right_most_bit(n, m))
