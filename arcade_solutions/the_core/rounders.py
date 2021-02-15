def rounders(n):
    length = len(str(n))
    power_of_ten = length - 1
    for i in range(length -1):
        n = int((n / 10) + 0.5)
    return n * (10 ** power_of_ten)


def rounders_short(n):
    x = 1
    while n > 10:
        n = (n + 5) // 10
        x *= 10
    return x * n


if __name__ == '__main__':
    n = 15
    rounders_short(n)
