def absolute_values_sum_minimization(a):
    i = (len(a)-1)//2
    return a[i]


if __name__ == '__main__':
    a = [2, 4, 7]
    print(absolute_values_sum_minimization(a))
    print(
        absolute_values_sum_minimization([2,3])
    )
