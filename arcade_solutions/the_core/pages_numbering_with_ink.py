def pages_numbering_with_ink(current, num_of_digits):
    remaining = num_of_digits
    for i in range(current, current + num_of_digits):
        x = len(str(i))
        remaining -= x
        if remaining < 0:
            return i
    return 0
