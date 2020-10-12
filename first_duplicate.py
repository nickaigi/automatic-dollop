def firstDuplicate(a):
    if len(a) == len(set(a)):
        return -1
    
    duplicates = {}
    for i, x in enumerate(a):
        for j, y in enumerate(a[(i + 1):], i+1):
            if x == y:
                if x in duplicates:
                    continue
                else:
                    duplicates[x] = j

    sorted_list = [k for k,v in sorted(duplicates.items(), key=lambda item: item[1])]
    return sorted_list[0]


if __name__ == '__main__':
    #a = [2, 1, 3, 5, 3, 2]
    #print(firstDuplicate(a))
    b = [1, 1, 2, 2, 1]
    print(firstDuplicate(b))
