def christmas_tree(n, h):
    tree = ['*', '*', '***']
    start = '*****'
    for i in range(n):
        tree.append(start)
        for j in range(1, h):
            tree.append('*' * (len(tree[-1]) + 2))
        start += '**'

    foot = '*' * h if h % 2 == 1 else '*' * h + '*'
    tree += [foot for i in range(n)]

    max_width = len(max(tree, key = len))
    return [i.center(max_width, ' ').rstrip() for i in tree]


if __name__ == '__main__':
    num = 1
    height = 3
    print(christmas_tree(num, height))
