def extract_each_kth(a, k):
    return [x for i, x in enumerate(a) if (i+1) % k != 0]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
    print(extract_each_kth(a, 3))
