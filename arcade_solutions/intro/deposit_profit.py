def deposit_profit(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        deposit = (100 + rate)/100 * deposit
        count += 1
    return count
