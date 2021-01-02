def longest_word(text):
    candidates = []
    word = ''
    res = ''
    
    for char in text:
        if not char.isalpha():
            candidates.append(word)
            word = ''
        if char.isalpha():
            word += char
    candidates.append(word)
    
    for i in range(len(candidates)):
        if len(candidates[i]) > len(res):
            res = candidates[i]
    return res


def longest_word_short(text):
    return max(re.split('[^[a-zA-Z]', text), key=len)


if __name__ == '__main__':
    text = 'Ready, steady, go!'
    longest_word(text)
