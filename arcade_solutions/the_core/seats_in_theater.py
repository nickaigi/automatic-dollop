def seats_in_theater(nCols, nRows, col, row):
    rows_blocked = nRows - row
    cols_blocked = nCols - col + 1  # you block the col you are on
    return rows_blocked * cols_blocked


if __name__ == '__main__':
    nCols = 16
    nRows = 11
    col = 5
    row = 3
    seats_in_theater(nCols, nRows, col, row)
