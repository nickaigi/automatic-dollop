def pair_of_shoes(shoes):
    shoes_dict = {}
    for s in shoes:
        if s[0] in shoes_dict.keys():
            shoes_dict[s[0]].append(s[1])
        else:
            shoes_dict[s[0]] = [s[1]]
    for p in shoes_dict:
        if len(shoes_dict[p]) != 2:
            return False
    return True


if __name__ == '__main__':
    shoes = [
        [0, 21], 
        [1, 23], 
        [1, 21], 
        [0, 23]
    ]
    print(pair_of_shoes(shoes))
