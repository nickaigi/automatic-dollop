def message_from_binary_code(code):
    res = ''
    for i in range(0, len(code), 8):
        num = int(code[i:i + 8], 2)
        res += chr(num)
    return res


if __name__ == '__main__':
    code =  '010010000110010101101100011011000110111100100001'
    print(message_from_binary_code(code))
