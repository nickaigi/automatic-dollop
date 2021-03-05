import math


def pages_numbering_with_ink(current, num_of_digits):
    while num_of_digits >= 0:
        num_of_digits -= int(math.ceil(math.log(current+1, 10)))
        current += 1
    return current - 2


if __name__ == '__main__':
    current = 1
    num_of_digits = 5
    print(pages_numbering_with_ink(current, num_of_digits))

