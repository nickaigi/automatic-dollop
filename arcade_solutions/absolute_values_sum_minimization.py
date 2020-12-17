def absolute_values_sum_minimization(a):
    diffs = []
    for i in range(len(a)):
        x = a[i]
        sum_i = 0
        for val in a:
            sum_i = sum_i + abs(x - val) 
        diffs.append(sum_i)
    return min(diffs)


if __name__ == '__main__':
    a = [2, 4, 7]
    print(absolute_values_sum_minimization(a))
