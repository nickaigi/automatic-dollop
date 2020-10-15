def check_rows(grid):
    for row in range(9):
        seen = set()
        for col in range(9):
            if grid[row][col] in seen:
                return False
            else:
                seen.add(grid[row][col])
    return True

def check_cols(grid):
    for col in range(9):
        seen = set()
        for row in range(9):
            if grid[row][col] in seen:
                return False
            else:
                seen.add(grid[row][col])
    return True

def check_sub_grids(grid):
    seen_grid_one = set()
    seen_grid_two = set()
    seen_grid_three = set()
    seen_grid_four = set()
    seen_grid_five = set()
    seen_grid_six = set()
    seen_grid_seven = set()
    seen_grid_eight = set()
    seen_grid_nine = set()

    for row in range(3):
        for col in range(3):
            if grid[row][col] in seen_grid_one:
                return False
            else:
                seen_grid_one.add(grid[row][col])

        for col in range(3, 6):
            if grid[row][col] in seen_grid_two:
                return False
            else:
                seen_grid_two.add(grid[row][col])


        for col in range(6, 9):
            if grid[row][col] in seen_grid_three:
                return False
            else:
                seen_grid_three.add(grid[row][col])


    for row in range(3, 6):
        for col in range(3):
            if grid[row][col] in seen_grid_four:
                return False
            else:
                seen_grid_four.add(grid[row][col])

        for col in range(3, 6):
            if grid[row][col] in seen_grid_five:
                return False
            else:
                seen_grid_five.add(grid[row][col])


        for col in range(6, 9):
            if grid[row][col] in seen_grid_six:
                return False
            else:
                seen_grid_six.add(grid[row][col])


    for row in range(6, 9):
        for col in range(3):
            if grid[row][col] in seen_grid_seven:
                return False
            else:
                seen_grid_seven.add(grid[row][col])

        for col in range(3, 6):
            if grid[row][col] in seen_grid_eight:
                return False
            else:
                seen_grid_eight.add(grid[row][col])


        for col in range(6, 9):
            if grid[row][col] in seen_grid_nine:
                return False
            else:
                seen_grid_nine.add(grid[row][col])
    return True

def sudoku2(grid):
    if check_rows(grid) and check_cols(grid) and check_sub_grids(grid):
        return True
    return False


if __name__ == '__main__':
    grid = [
        ['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.'],
    ]
    print(sudoku2(grid))
