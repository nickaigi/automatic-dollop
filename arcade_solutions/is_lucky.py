def is_lucky(n):
    s = str(n)
    half = len(s)//2
    left, right = s[:half], s[half:]
    return sum(map(int, left)) == sum(map(int, right))
