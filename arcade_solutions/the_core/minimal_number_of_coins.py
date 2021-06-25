def minimal_number_of_coins(coins, price):
    bal = price
    count = len(coins)
    while bal > 0:
        bal -= max(coins[:count])
    return 1
