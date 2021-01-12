def max_multiple(divisor, bound):
    n = 1
    for i in range(divisor, bound + 1):
        if i % divisor == 0:
            n = i
    return n


if __name__ == '__main__':
    divisor = 3
    bound = 10
    max_multiple(divisor, bound)
