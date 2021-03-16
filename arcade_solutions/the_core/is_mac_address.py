import string


def is_mac_address(s):
    if len(s) != 17:
        return False
    return all(c in string.hexdigits + '-' for c in s) and s.count('-') == 5
