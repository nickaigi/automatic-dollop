def firstDuplicate(a):
    if len(a) == len(set(a)):
        return -1
    
    seen = set()
    for i in a:
        if i in seen:
            return i
        else:
            seen.add(i)

if __name__ == '__main__':
    #a = [2, 1, 3, 5, 3, 2]
    #print(firstDuplicate(a))
    b = [1, 1, 2, 2, 1]
    print(firstDuplicate(b))
