def array_packing(a):
    return sum([n << 8 * i for i, n in enumerate(a)])


if __name__ == '__main__':
    a = [24, 85, 0]
    print(array_packing(a))
