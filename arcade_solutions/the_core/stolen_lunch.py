import string


def stolen_lunch(note):
    s = string.ascii_lowercase
    res = ''
    for c in note:
        if c.isdigit():
            res += s[int(c)]
        else:
            res += c
    return res
