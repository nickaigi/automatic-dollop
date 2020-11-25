def possibleSums(coins, quantity):
    sums = {0}
    for c, q in zip(coins, quantity):
        new = {}
        for i in range(1, q+1):
            for sum_ in sums:
                temp = sum_ + i * c
                if temp not in sums:
                    new[temp] = temp
        sums.update(new)
    
    return len(sums) - 1

def possible_sums_concise(coins, quantity):
    sums = {0}
    for c, q in zip(coins, quantity):
        sums = {x + i * c for x in sums for i in range(q + 1)}

    return len(sums) - 1


if __name__ == '__main__':
    coins = [10, 50, 100]
    quantity = [1, 2, 1]
    
    possibleSums(coins, quantity)
