import string

ALPHABET =  string.ascii_lowercase


def longest_word(text):
    words = text.split(' ')
    if len(words) == 1:
        return text
    for w in words:
        for ch in w:
            # we need an index
            pass


if __name__ == '__main__':
    text = 'Ready, steady, go!'
    longest_word(text)
