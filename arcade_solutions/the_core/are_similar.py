def are_similar(a, b):
    for x in range(len(a)):
        if a[x] != b[x]:
            return False
    return True


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [2, 1, 3]

    print(are_similar(a, b))
