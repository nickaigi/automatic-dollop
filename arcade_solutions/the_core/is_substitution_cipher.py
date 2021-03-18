def is_substitution_cipher(s1, s2):
    return all(s1.count(c) == s2.count(c) for c in s1)
