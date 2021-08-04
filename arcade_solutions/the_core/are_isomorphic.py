def are_isomorphic(a1, a2):
    return False


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
