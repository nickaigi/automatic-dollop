import string


def encrypt(msg):
    a = string.ascii_lowercase
    cipher_text = []
    s = 0
    for c in msg:
        s += a.find(c)
        cipher_text.append(a[s % 26])
    return ''.join(cipher_text)


def cipher_26(message):
    return ''


if __name__ == '__main__':
    message = 'taiaiaertkixquxjnfxxdh'
    print(message == encrypt('thisisencryptedmessage'))
    #print(cipher_26(message))
