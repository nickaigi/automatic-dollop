def check_numbers(numbers):
    seen = set()
    for num in numbers:
        if num == '.':
            continue
        if num in seen:
            return False
        seen.add(num)
    return True

def check_sub_grids(grid):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not check_numbers(
                grid[row][col:col+3] + grid[row+1][col:col +3] + grid[row+2][col:col+3]
            ):
                return False
    return True

        
def sudoku2(grid):
    for row in grid:
        if not check_numbers(row):
            return False

    for col in range(9):
        if not check_numbers([row[col] for row in grid]):
            return False

    if not check_sub_grids(grid):
        return False
    return True


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
