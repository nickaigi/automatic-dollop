def is_smooth(arr):
    mid = 0
    mid_one = 0
    mid_two = 0
    arr_len = len(arr)
    if len(arr) % 2 != 0:
        mid = arr[arr_len // 2]
    else:
        mid_one = arr_len // 2
        mid_two = arr_len // 2 - 1
        print(mid_one, mid_two)
        mid = arr[mid_one] + arr[mid_two]
    if mid == arr[0] and mid == arr[arr_len - 1]:
        return True
    return False


if __name__ == '__main__':
    arr = [7, 2, 2, 5, 10, 7]
    print(is_smooth(arr))
