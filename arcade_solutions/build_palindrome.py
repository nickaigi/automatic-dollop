def build_palindrome(st):
    half = len(st) // 2
    if st != st[::-1]:
        new_st = st + st[:half + 1][::-1]
        return new_st
    return st
