def firstDuplicate(a):
    if len(a) == len(set(a)):
        return -1
    
    duplicates = {}
    for i, x in enumerate(a):
        for j, y in enumerate(a[(i + 1):], i+1):
            if x == y:
                duplicates[x] = j

    sorted_list = []
    for k,v in duplicates.items():
        sorted_list.append(v)


if __name__ == '__main__':
    a = [2, 1, 3, 5, 3, 2]
    print(firstDuplicate(a))
