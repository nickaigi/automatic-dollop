def switch(array, idx):
    for i in range(idx + 1):
        if array[i] == 1:
            array[i] = 0
        else:
            array[i] = 1
    return array


def switch_lights(a):
    result = a.copy()
    for idx, c in enumerate(a):
        if c == 1:
            result = switch(result, idx)
    return result


if __name__ == '__main__':
    a = [1, 1, 1, 1, 1]
    print(switch_lights(a))
