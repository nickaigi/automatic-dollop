import string


def encrypt(msg):
    a = string.ascii_lowercase
    cipher_text = []
    s = 0
    for c in msg:
        s += a.find(c)
        cipher_text.append(a[s % 26])
    return ''.join(cipher_text)


def cipher_26(msg):
    a = string.ascii_lowercase
    s, n = '', 0
    for i, c in enumerate(msg):
        s += a[(a.find(c) - n) % 26]
        n += (a.find(c) - n) % 26
    return s


if __name__ == '__main__':
    message = 'taiaiaertkixquxjnfxxdh'
    print(message == encrypt('thisisencryptedmessage'))
    print(cipher_26(message))
