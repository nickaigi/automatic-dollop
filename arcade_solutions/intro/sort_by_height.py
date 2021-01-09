def sort_by_height(a):
    l = sorted([i for i in a if i > 0])
    for n, i in enumerate(a):
        if i == -1:
            l.insert(n, i)
    return l


if __name__ == '__main__':
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    sort_by_height(a)
