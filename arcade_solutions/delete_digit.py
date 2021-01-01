def delete_digit(n):
    results = []
    digits = str(n)
    for i,c in enumerate(digits):
        if i == 0:
            results.append(int(digits[1: len(digits)]))
        else:
            results.append(int(f'{digits[0: i]}{digits[i+1: len(digits)]}'))
    return max(results)


if __name__ == '__main__':
    n = 152
    print(delete_digit(n))
    n = 1001
    print(delete_digit(n))
