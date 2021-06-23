import string


def alphabet_subsequence(s):
    for c in s:
        if c not in string.ascii_lowercase:
            return False
    return True


if __name__ == '__main__':
    s = 'effg'
    print(alphabet_subsequence(s))
