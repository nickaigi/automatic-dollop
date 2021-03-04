def pages_numbering_with_ink(current, num_of_digits):
    remaining = num_of_digits
    current -= 1  # we have to print the current page
    while remaining > 0:
        current += 1
        x = len(str(current))
        remaining -= x
    return current
