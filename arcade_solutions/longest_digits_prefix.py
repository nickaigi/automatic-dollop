def longest_digits_prefix(s):
    res = []
    for ch in s:
        if ch.isdigit():
            res.append(ch)
    return ''.join(res)
