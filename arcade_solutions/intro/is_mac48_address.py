import string


def is_mac48_address(s):
    address = s.split('-')
    if len(address) != 6:
        return False

    if len(s) != 17:  #!+ alternative is to check for len(grp) == 2
        return False

    for grp in address:
        for ch in grp:
            if ch not in string.hexdigits:
                return False
    return True


if __name__ == '__main__':
    s = '00-1B-63-84-45-E6'
    is_mac48_address(s)
