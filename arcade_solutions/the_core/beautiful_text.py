def beautiful_text(s, l, r):
    for w in range(l, r+1):
        i = w
        while i < len(s):
            if s[i] != ' ':
                break
            i += w + 1
        if i == len(s):
            return True
    return False


if __name__ == '__main__':
    s = 'Look at this example of a correct text'
    l = 5
    r = 15
    print(beautiful_text(s, l, r))
