def sum_up_numbers(s):
    total = 0
    digits = []
    for ch in s:
        if ch.isdigit():
            digits.append(ch)
    print(digits)
    return total


if __name__ == '__main__':
    s = '2 apples, 12 oranges'
    sum_up_numbers(s)
