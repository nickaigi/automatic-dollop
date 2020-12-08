def is_ipv4_address(s):
    ip = s.split('.')
    if len(ip) != 4:
        return False
    for i in range(len(ip)):
        if not ip[i].isnumeric():
            return False
        elif len(ip[i]) > 1 and ip[i][0] == '0':
            return False
        elif int(ip[i]) not in range(256):
            return False
    return True
