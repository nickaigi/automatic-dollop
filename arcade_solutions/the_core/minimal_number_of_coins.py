def minimal_number_of_coins(coins, price):
    bal = price
    index = len(coins)
    count = 0
    while bal > 0:
        if bal >= max(coins[:index]):
            bal -= max(coins[:index])
            count += 1
        else:
            index -= 1
    return count



if __name__ == '__main__':
    coins = [1, 2, 10]
    price = 28
    print(minimal_number_of_coins(coins, price))
