def decipher(cipher):
    cipher = cipher.replace('97', '097').replace('98', '098').replace('99', '099')
    return ''.join(chr(int(cipher[i:i+3])) for i in range(0, len(cipher), 3))
        

if __name__ == '__main__':
    cipher = '10197115121'
    print(decipher(cipher))
