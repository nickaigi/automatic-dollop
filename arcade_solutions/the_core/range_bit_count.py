def range_bit_count(a, b):
    return sum(bin(x).count('1') for x in range(a, b+1))

if __name__ == '__main__':
    a = 2
    b = 7
    range_bit_count(a, b)

