def is_ipv4_address(s):
    ips = inputString.split('.')
    if len(ips) != 4:
        return False
    for count, ip in enumerate(ips):
        try:
            if int(ip) == 0 and count == 0:
                continue
            if ip == '' or int(ip) > 255:
                return False
            if ip.startswith('0') and ip != '0':
                return False
        except Exception:
            return False
    return True
