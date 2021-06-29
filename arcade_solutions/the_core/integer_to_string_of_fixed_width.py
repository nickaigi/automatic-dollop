def integer_to_string_of_fixed_width(number, width):
    return str(number).zfill(width)[-width:]


def integer_to_string_of_fixed_width_old(number, width):
    s = str(number)
    if len(s) == width:
        return s
    if len(s) > width:
        return s[len(s) - width:]
    else:
        d = width - len(s)
        for i in range(d):
            s = '0' + s
    return s


if __name__ == '__main__':
    number = 1234
    width = 2
    print(integer_to_string_of_fixed_width(number, width))
