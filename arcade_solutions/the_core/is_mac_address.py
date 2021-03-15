import string


def is_mac_address(s):
    return all(c in string.hexdigits + '-' for c in s)
