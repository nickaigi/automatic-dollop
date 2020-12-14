import string


def alphabetic_shift(s):
    alphabet = list(string.ascii_lowercase)
    answer = []
    for c in s:
        i = alphabet.index(c)
        if c == 'z':
            answer.append('a')
        else:
            answer.append(alphabet[i+1])
    return ''.join(answer)


if __name__ == '__main__':
    s  = 'crazy'
    print(alphabetic_shift(s))
