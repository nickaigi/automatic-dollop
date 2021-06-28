import string


def timed_reading(max_length, text):
    count = 0
    text = text.translate(str.maketrans('', '', string.punctuation))
    for w in text.split(' '):
        if w and len(w) <= max_length:
            count += 1
    return count


if __name__ == '__main__':
    max_length = 4
    text = "The Fox asked the stork, 'How is the soup?'"
    print(timed_reading(max_length, text))
