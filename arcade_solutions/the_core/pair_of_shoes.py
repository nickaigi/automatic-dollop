def pair_of_shoes(shoes):
    a = []
    b = []
    for s in shoes:
        if s[0] == 0:
            a.append(s[1])
        else:
            b.append(s[1])
    return sorted(a) == sorted(b)

if __name__ == '__main__':
    shoes = [
        [0, 21], 
        [1, 23], 
        [1, 21], 
        [0, 23]
    ]
    print(pair_of_shoes(shoes))
