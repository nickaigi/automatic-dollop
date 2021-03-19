def create_anagram(s, t):
    count = 0
    for c in t:
        if c not in s:
            count += 1
    return count
