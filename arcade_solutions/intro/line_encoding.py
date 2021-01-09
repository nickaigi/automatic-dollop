from itertools import groupby


def line_encoding_short(s):
    soln = ''
    for k, g in groupby(s):
        y = len(list(g))
        if y == 1:
            soln += k
        else:
            soln += str(y) + k
    return soln


def line_encoding(s):
    count = 1
    result = []
    for char in range(1, len(s)):
        if s[char] == s[char - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count) + s[char - 1])
            else:
                result.append(s[char - 1])
            count = 1
    if s[len(s) - 1] == s[len(s) - 2]:
        result.append(str(count) + s[len(s) -1])
    else:
        result.append(s[len(s) - 1])
    return ''.join(result)


if __name__ == '__main__':
    s = 'aabbbc'
    print(line_encoding_short(s))
