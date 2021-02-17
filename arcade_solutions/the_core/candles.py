def candles(candles_number, make_new):
    total = 0
    left_over = 0
    while candles_number > 0:
        total += candles_number
        left_over += candles_number
        candles_number = left_over // make_new
        left_over = left_over % make_new
    return total


def candles_short(candles_number, make_new):
    return candles_number +(candles_number - 1) // (make_new - 1)


if __name__ == '__main__':
    candles_number = 5
    make_new = 2
    candles_short(candles_number, make_new)
