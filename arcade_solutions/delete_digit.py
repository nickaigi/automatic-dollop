def delete_digit(n):
    digits = str(n)
    for i,c in enumerate(digits):
        if i == 0:
            print(digits[1: len(digits)])
        else:
            print(digits[0: i], digits[i+1: len(digits)]


if __name__ == '__main__':
    n = 152
    print(delete_digit(n))
    n = 1001
    print(delete_digit(n))
