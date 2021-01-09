def areSimilar(a, b, swaps=0):
    if a == b:
        return True

    mismatched = []
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatched.append(i)
    if len(mismatched) == 2:
        if a[mismatched[0]] == b[mismatched[1]] and a[mismatched[1]] == b[mismatched[0]]:
            return True
    return False


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [2, 1, 3]

    a1 = [2, 3, 1]
    b1 = [1, 3, 2]

    a2 = [1, 2, 3]
    b2 = [1, 10, 2]

    print(areSimilar(a, b))
    print(areSimilar(a1, b1))
    print(areSimilar(a2, b2))
