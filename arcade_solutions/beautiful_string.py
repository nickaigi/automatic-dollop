import string


ALPHABET = string.ascii_lowercase


def is_beautiful_string(s):
    counts = []
    for ch in ALPHABET:
        if ch in s:
            counts.append(s.count(ch))
    for i in range(len(counts) - 1):
        if counts[i] < counts[i+1]:
            return False
    return True


if __name__ == '__main__':
    s = 'bbbaacdafe'
    print(is_beautiful_string(s))
    s = 'bbc'
    print(is_beautiful_string(s))  # should print False, because there are more b's than 'a'
