def increase_number_roundness(n):
    while n % 10 == 0:
        n /= 10
    else:
        n /= 10
    return True if n != 0  else False


if __name__ == '__main__':
    n = 902200100
    print(increase_number_roundness(n))
