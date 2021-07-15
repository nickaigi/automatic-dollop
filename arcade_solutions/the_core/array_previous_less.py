def last_small(arr, current):
    l = len(arr)
    smallest = -1
    if l < 1:
        return smallest
    if arr[l - 1] < current:
        smallest = arr[l - 1]
    return smallest


def array_previous_less(items):
    new_arr = []
    for i in range(len(items)):
        new_arr.append(last_small(items[:i], items[i]))
    return new_arr


if __name__ == '__main__':
    items = [3, 5, 2, 4, 5]
    print(array_previous_less(items))
