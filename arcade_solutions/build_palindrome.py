def build_palindrome(st):
    half = len(st) // 2
    if st != st[::-1]:
        new_st = st + st[:half][::-1]
        return new_st
    return st


if __name__ == '__main__':
    st = 'abcdc'
    print(build_palindrome(st))
