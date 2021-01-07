def message_from_binary_code(code):
    for i in range(0, len(code), 8):
        print(code[i:i + 8])


if __name__ == '__main__':
    code =  '010010000110010101101100011011000110111100100001'
    print(message_from_binary_code(code))
