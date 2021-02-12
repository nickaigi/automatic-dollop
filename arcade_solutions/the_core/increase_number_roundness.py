def increase_number_roundness(n):
    return '0' in str(n).rstrip('0')


if __name__ == '__main__':
    n = 902200100
    print(increase_number_roundness(n))
