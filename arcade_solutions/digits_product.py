def digits_product_other(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    n = []
    while 1 < product:
        for d in range(9, 1, -1):
            if product % d == 0:
                product /= d
                n.append(d)
                break
        else:
            return -1
    return int(''.join(map(str, sorted(n))))


def digits_product(product):
    for i in range(1, 10000):
        number = str(i)
        total = 1
        for char in number:
            total *= int(char)
        if total == product:
            return i
    return -1


if __name__ == '__main__':
    product = 12
    print(digits_product(product))
    print(digits_product_other(19))
