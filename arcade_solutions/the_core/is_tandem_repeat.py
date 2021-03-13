def is_tandem_repeat(s):
    return s[:len(s)//2] == s[len(s)//2:]
