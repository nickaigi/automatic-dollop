import string

ALPHABET =  string.ascii_lowercase


def longest_word(text):
    words = text.split(' ')
    candidates = []
    longest = ''
    if len(words) == 1:
        return text
    for w in words:
        if w.isaplpha():
            for i, ch in enumerate(w):
                j = ALPHABET.index(ch.lower())
                if w[i + 1] == ALPHABET[j+1]:
                    if w not in candidates:
                        candidates.append(w)
    return max(len(w) for w in candidates)


if __name__ == '__main__':
    text = 'Ready, steady, go!'
    longest_word(text)
