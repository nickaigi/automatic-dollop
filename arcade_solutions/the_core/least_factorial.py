def least_factorial(n):
    k = 1
    loop = 1
    while k < n:
        k *= loop
        loop += 1
    return k


if __name__ == '__main__':
    n = 17
    print(least_factorial(n))
