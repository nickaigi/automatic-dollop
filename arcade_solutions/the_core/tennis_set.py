def tennis_set(s1, s2):
    n1 = min(s1, s2)
    n2 = max(s1, s2)
    if n2 == 6:
        return n1 < 5
    return n2 == 7 and n1 >= 5 and n1 < n2
