def array_previous_less(items):
    less = [-1 for _ in items]
    for i in range(len(items)):
        for j in range(i-1, -1, -1):
            if items[i] > items[j]:
                less[i] = items[j]
                break
    return less

if __name__ == '__main__':
    items = [3, 5, 2, 4, 5]
    print(array_previous_less(items))
