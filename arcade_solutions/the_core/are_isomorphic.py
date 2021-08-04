def are_isomorphic(a1, a2):
    return [len(i) for i in a1] == [len(i) for i in a2]


if __name__ == '__main__':
    array1 = [
        [1, 1, 1],
        [0, 0]
    ]

    array2 = [
        [2, 1, 1],
        [2, 1]
    ]

    print(are_isomorphic(array1, array2))
