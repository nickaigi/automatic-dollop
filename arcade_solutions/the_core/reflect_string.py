import string


def reflect_sting(s):
    result = ""
    for c in s:
        i = 1 + string.ascii_lowercase.find(c)
        result += string.ascii_lowercase[-i]
    return result


if __name__ == '__main__':
    s = 'name'
    print(reflect_sting(s))
