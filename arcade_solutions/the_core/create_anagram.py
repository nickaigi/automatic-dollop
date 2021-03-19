def create_anagram(s, t):
    count = 0
    found = set()
    for ch in s:
        if ch not in found:
            found.update(ch)
            if t.count(ch) != s.count(ch):
                count += abs(t.count(ch) - s.count(ch))
    return count



if __name__ == '__main__':
    s = 'AABAA'
    t = 'BBAAA'
    print(create_anagram(s, t))
