def addition_without_carrying(a, b):
    for x, y in zip(str(a), str(b)):
        print(x, y)
    return 0


if __name__ == '__main__':
    a = 456
    b = 1734
    print(addition_without_carrying(a, b))
