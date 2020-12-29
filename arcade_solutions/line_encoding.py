def line_encoding(s):
    chars = set(s)
    result = []
    for c in chars:
        num_c = s.count(c)
        if num_c > 1:
            result.append(f'{num_c}{c}')
        else:
            result.append(c)
    return ''.join(result)


if __name__ == '__main__':
    s = 'aabbbc'
    print(line_encoding(s))
