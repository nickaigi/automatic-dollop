import string


def stolen_lunch(note):
    tab = str.maketrans('0123456789abcdefghij', 'abcdefghij0123456789')
    return str(note).translate(tab)

if __name__ == '__main__':
    note = "you'll n4v4r 6u4ss 8t: cdja"
    print(stolen_lunch(note))
