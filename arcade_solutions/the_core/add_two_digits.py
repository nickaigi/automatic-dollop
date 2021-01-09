def add_two_digits(n):
    tens = n // 10
    ones = n % 10
    return tens + ones


if __name__ == '__main__':
    n = 29
    print(add_two_digits(n))
