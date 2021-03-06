import string


def new_numeral_system(number):
    s = string.ascii_uppercase
    i = s.find(number)
    d = []
    for x, y in zip(s[:i+1], reversed(s[:i+1])):
        if x <= y:
            d.append(f'{x} + {y}')
    return d


def new_numeral_system_old(number):
    if number == 'A':
        return ['A + A']
    char_value = {
        char: value for value, char in enumerate(string.ascii_uppercase)
    }
    value_char = {
        value: char for value, char in enumerate(string.ascii_uppercase)
    }

    n = char_value[number]
    result = []
    k = -1  # placeholder
    count = 0
    if n % 2 == 0:
        k = n / 2
    else:
        k = n // 2 + 1

    for i in reversed(range(n + 1)):
        result.append(f'{value_char[count]} + {value_char[i]}')
        if i == k:
            break
        else:
            count += 1
    return result


if __name__ == '__main__':
    number = 'G'
    print(new_numeral_system(number))
