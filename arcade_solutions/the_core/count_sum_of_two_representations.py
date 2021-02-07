def count_sum_of_two_representations(n, l, r):
    if (2 * r < n) or (2 * l > n):
        return 0
    _min = max(l, n - r)
    _max = min(r, n - l)
    mid = (_max + _min) // 2
    return mid - _min + 1


def count_sum_of_two_representations_short(n, l, r):
    return sum(1 for a in range(l, r+1) if l <= a <= n - a <= r)


if __name__ == '__main__':
    n = 6
    l = 2
    r = 4
    count_sum_of_two_representations_short(n, l, r)
