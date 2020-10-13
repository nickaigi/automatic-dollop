def firstNotRepeatingCharacter(s):
    _array = list(s)
    found_chars = []
    not_found = '_'
    
    for i, _char in enumerate(_array):
        if _char not in found_chars:
            found_chars.append(_char)
        if _char not in _array[(i+1):]:
            return _char
    return '_


if __name__ == '__main__':
    pass
