def numbers_grouping(a):
    return len(set([(x-1)//10000 for x in a])) + len(a)


if __name__ == '__main__':
    a = [20000, 239, 10001, 999999, 10000, 20566, 29999]
    print(numbers_grouping(a))
