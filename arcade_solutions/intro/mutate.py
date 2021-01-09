def mutateTheArray(n, a):
    b = []
    for i,num in enumerate(a):
        x = 0 if i == 0 else a[(i-1)]
        y = 0 if i >= n - 1 else a[(i+1)]

        b.append(x + a[i] + y)
    return b


if __name__ == '__main__':
    n = 5
    a = [4, 0, 1, -2, 3]
    print(mutateTheArray(n, a))
