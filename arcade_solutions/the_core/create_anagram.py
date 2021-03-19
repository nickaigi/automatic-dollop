def create_anagram(s, t):
    s = list(s)
    for ch in t:
        if ch in s:
            s.remove(ch)
    return len(s)


def create_anagram_short(s, t):
    return sum(max(0, s.count(ch) - t.count(ch)) for ch in set(s))


if __name__ == '__main__':
    s = 'AABAA'
    t = 'BBAAA'
    print(create_anagram_short(s, t))
