def late_ride(n):
    digits = []
    hours = n // 60
    minutes = n % 60

    digits.append(hours//10)
    digits.append(hours % 10)
    digits.append(minutes//10)
    digits.append(minutes % 10)

    print(digits)
    return sum(digits)


if __name__ == '__main__':
    n = 240
    late_ride(n)
