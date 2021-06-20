def house_numbers_sum_old(arr):
    s = 0
    for x in arr:
        if x != 0:
            s += x
        else:
            break
    return s


def house_numbers_sum(arr):
    return sum(arr[:arr.index(0)])
