import math


def prod_arr(arr):
    return [math.prod(arr[i: i+2]) for i in range(0, len(arr), 2)]


def sum_arr(arr):
    return [sum(arr[i: i+2]) for i in range(0, len(arr), 2)]


def array_conversion(arr):
    new_arr = arr
    is_odd = True
    while len(new_arr) != 1:
        if is_odd:
            new_arr = sum_arr(new_arr)
            is_odd = False
        else:
            new_arr = prod_arr(new_arr)
            is_odd = True
    return new_arr[0]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(array_conversion(arr))
