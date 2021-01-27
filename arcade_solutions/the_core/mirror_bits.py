def mirror_bits(a):
    return int(str(bin(a))[2:][::-1], 2)


if __name__ == '__main__':
    a = 97
    mirror_bits(a)
