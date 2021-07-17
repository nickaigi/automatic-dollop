def pair_of_shoes(shoes):
    shoes_dict = {}
    for pair in shoes:
        if pair[1] in shoes_dict:
            shoes_dict[pair[1]].append(pair[0])
        else:
            shoes_dict[pair[1]] = [pair[0]]
    print(shoes_dict)
    return True


if __name__ == '__main__':
    shoes = [
        [0, 21], 
        [1, 23], 
        [1, 21], 
        [0, 23]
    ]
    print(pair_of_shoes(shoes))
