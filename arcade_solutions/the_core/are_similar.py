def are_similar(a, b):
    return sorted(a) == sorted(b) and sum(i != j for i, j in zip(a, b)) < 3


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [2, 1, 3]

    print(are_similar(a, b))
