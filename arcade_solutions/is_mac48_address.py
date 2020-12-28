def is_mac48_address(s):
    address = s.split('-')
    if len(address) != 6:
        return False
    return True
