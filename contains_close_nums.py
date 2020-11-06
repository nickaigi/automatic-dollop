def contains_close_nums(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d.keys():
            if abs(d[nums[i]] - i) <= k:
                return True
            else:
                d[nums[i]] = i
    return False


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 5, 2]
    k = 3

    contains_close_nums(nums, k)
