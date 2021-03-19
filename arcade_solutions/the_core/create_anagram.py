def create_anagram(s, t):
    s = list(s)
    for ch in t:
        if ch in s:
            s.remove(ch)
    return len(s)


if __name__ == '__main__':
    s = 'AABAA'
    t = 'BBAAA'
    print(create_anagram(s, t))
