def replace_middle(arr):
    arr_len = len(arr)
    if arr_len % 2 == 0:
        result = []
        mid_one = arr_len // 2 - 1
        mid_two = mid_one + 1
        for i in range(arr_len):
            if i == mid_one:
                result.append(arr[mid_one] + arr[mid_two])
            elif i == mid_two:
                continue
            else:
                result.append(arr[i])
        return result
    return arr


def replace_middle_short(arr):
    n = len(arr)
    if not n & 1:
        mid = arr[n//2] + arr[n//2 -1]
        arr[n//2-1:n//2+1] = [mid]
    return arr


if __name__ == '__main__':
    arr = [7, 2, 2, 5, 10, 7]
    print(replace_middle_short(arr))
