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


def sudoku(grid):
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
        [1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5],
    ]
    sudoku(grid)  # True
    grid = [
        [1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5],
    ]
    sudoku(grid)  # False
