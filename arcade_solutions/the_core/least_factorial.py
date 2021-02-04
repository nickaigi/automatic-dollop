def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def least_factorial(n):
    k = 1
    loop = 1
    while k < n:
        k = fact(loop)
        loop += 1
    return k


if __name__ == '__main__':
    n = 17
    print(least_factorial(n))
