def cyclic_string(s):
    for i in range(0, len(s)):
        sub = s[0:i+1]
        multiplier = len(s) // (i+1) + 1
        if s in sub * multiplier:
            return i + 1


if __name__ == '__main__':
    s = 'cabca'
    print(cyclic_string(s))
