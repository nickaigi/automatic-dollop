def make_array_consecutive(arr):
    arr.sort()
    start = arr[0]
    stop = arr[-1]
    count = 0
    for i in range(start, stop):
        if i not arr:
            count += 1
    return count


def make_array_consecutive(arr):
    return max(arr) - min(arr) - len(arr) + 1
