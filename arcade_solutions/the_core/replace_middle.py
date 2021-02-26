def replace_middle(arr):
    arr_len = len(arr)
    if arr_len % 2 == 0:
        mid_one = arr_len // 2 - 1
        mid_two = mid_one + 1
        print(arr, mid_one, mid_two)
    return arr


if __name__ == '__main__':
    arr = [7, 2, 2, 5, 10, 7]
    print(replace_middle(arr))
