import re


def tokenize(s):
    tokens = re.findall('\d+|.', s)
    return (
        [
            (0, int(token)) if token.isdigit() else (1, token) for token in tokens
        ],
        [-len(token) for token in tokens]
    )


def alphanumeric_less(s1, s2):
    return tokenize(s1) < tokenize(s2)
    

if __name__ == '__main__':
    s1 = 'a'
    s2 = 'a1'
    print(alphanumeric_less(s1, s2))
