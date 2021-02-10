def addition_without_carrying(a, b):
    result = 0
    ten_power = 1
    while a > 0 or b > 0:
        result += ten_power * ((a + b) % 10)
        a //= 10
        b //= 10
        ten_power *= 10
    return result


if __name__ == '__main__':
    a = 456
    b = 1734
    print(addition_without_carrying(a, b))
