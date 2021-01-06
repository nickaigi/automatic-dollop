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
