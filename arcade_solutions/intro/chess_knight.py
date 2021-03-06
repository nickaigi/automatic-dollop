COLS = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
ROWS = [1, 2, 3, 4, 5, 6, 7, 8]
BOARD = [ col + str(row) for row in ROWS for col in COLS]


def can_move(col_delta, row_delta, cell):
    col = cell[0]
    row = int(cell[1])
    new_col_index = COLS.index(col) + col_delta
    if new_col_index < 0:
        return False
    new_row = row + row_delta
    new_cell = ''
    try:
        new_cell = COLS[new_col_index] + str(new_row)
    except IndexError:
        print(f'{cell} attacks {new_cell}', False)
        return False
    if new_cell in BOARD:
        print(f'{cell} attacks {new_cell}', True)
        return True


def chess_knight(cell):
    count = 0
    if can_move(2, 1, cell):
        count += 1
    if can_move(1, 2, cell):
        count += 1
    if can_move(-1, 2, cell):
        count += 1
    if can_move(-2, 1, cell):
        count += 1
    if can_move(-2, -1, cell):
        count += 1
    if can_move(-1, -2, cell):
        count += 1
    if can_move(1, -2, cell):
        count += 1
    if can_move(2, -1, cell):
        count += 1
    return count


def chess_knight_short(cell):
    moves = 8
    if cell[0] == 'b' or cell[0] == 'g':
        moves -= 2
    if cell[1] == '2' or cell[1] == '7':
        moves -= 2
    if cell[0] == 'a' or cell[0] == 'h':
        moves /= 2
    if cell[1] == '1' or cell[1] == '8':
        moves /= 2
    return int(moves)


if __name__ == '__main__':
    cell = 'd5'
    moves = chess_knight_short(cell)
    print(moves)
    cell = 'a1'
    moves = chess_knight_short(cell)
    print(moves)
