def array_max_consecutive_sum(arr, k):
    result_array = []
    for i in range(len(arr) - (k-1)):
        temp = []
        for j in range(i, i+k):
            temp.append((arr[j]))
        result_array.append(sum(temp))
    return max(result_array)


if __name__ == '__main__':
    arr = [2, 3, 5, 1, 6]
    k = 2
    print(array_max_consecutive_sum(arr, k))
