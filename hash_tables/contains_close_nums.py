def contains_close_nums(nums, k):
    groups = {}
    for i in range(len(nums)):
        groups.setdefault(nums[i], []).append(i)

    for l in groups.values():
        if len(l) > 1:
            diff = min([j-i for i, j in zip(l[:-1], l[1:])])
            if abs(diff) <= k:
                return True
    return False


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 5, 2]
    k = 3

    contains_close_nums(nums, k)

    nums = [1, 0, 1, 1]
    k = 1
    contains_close_nums(nums, k)
