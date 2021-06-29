def are_similar(a, b):
    return a == b  or False


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [2, 1, 3]

    print(are_similar(a, b))
