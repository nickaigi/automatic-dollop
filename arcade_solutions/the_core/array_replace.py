def array_replace_long(input_array, elem_to_replace, sub_elem):
    result = []
    for x in input_array:
        if x == elem_to_replace:
            result.append(sub_elem)
        else:
            result.append(x)
    return result


def array_replace(input_array, elem_to_replace, sub_elem):
    return [sub_elem if i == elem_to_replace else i for i in input_array]


if __name__ == '__main__':
    input_array = [1, 2, 1]
    elem_to_replace = 1
    sub_elem = 3
    res = array_replace(input_array, elem_to_replace, sub_elem)
    print(res)
