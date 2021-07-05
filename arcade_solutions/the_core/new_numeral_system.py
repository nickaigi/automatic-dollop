import string

def new_numeral_system(number):
    alphabet = {}
    for i, char in enumerate(string.ascii_uppercase):
        alphabet[char] = i
    print(alphabet[number])
    return ["0"]


if __name__ == '__main__':
    number = 'G'
    print(new_numeral_system(number))

