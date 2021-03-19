def is_substitution_cipher(s1, s2):
    return len(set(zip(s1, s2))) == len(set(s1)) == len(set(s2))


if __name__ == '__main__':
    s1 = 'aaxxaaz'
    s2 = 'aazzaay'
    print(is_substitution_cipher(s1, s2))
