def first_not_repeating_character(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'


if __name__ == '__main__':
    s = 'abacabad'
    print(first_not_repeating_character(s))
