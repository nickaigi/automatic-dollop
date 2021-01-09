def array_max_consecutive_sum_short(a, k):
    c = m = sum(a[:k])
    for i in range(len(a) - k):
        c = c + a[i + k] - a[i]
        m = max(c, m)
    return m


def array_max_consecutive_sum(a, k):
    # works, but has O(n^2) time which is undesirable
    result_array = []
    for i in range(len(a) - (k-1)):
        temp = []
        for j in range(i, i+k):
            temp.append((a[j]))
        result_array.append(sum(temp))
    return max(result_array)


if __name__ == '__main__':
    arr = [2, 3, 5, 1, 6]
    k = 2
    print(array_max_consecutive_sum(arr, k))
