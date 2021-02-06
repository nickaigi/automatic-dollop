def count_sum_of_two_representations(n, l, r):
    if (2 * r < n) or (2 * l > n):
        return 0
    _min = max(l, n - r)
    _max = min(r, n - l)
    mid = (_max + _min) // 2
    return mid - _min + 1
