def first_reverse_old(arr):
    result = []
    if arr:
        l = len(arr)
        first = arr[0]
        last = arr[l - 1]
        for i in range(l):
            if i == 0:
                result.append(last)
            elif i == l - 1:
                result.append(first)
            else:
                result.append(arr[i])
    return result


def first_reverse_try(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr
