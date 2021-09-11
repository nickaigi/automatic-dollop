def sudoku(grid):
    nine = set(range(1, 10))

    def row(i):
        return set(grid[i])

    def col(j):
        return set(grid[i][j] for i in range(9))

    def cell(x):
        return set(grid[x - x % 3 + i // 3][(x % 3) * 3 + i % 3] for i in range(9))

    return all(nine == row(i) == col(i) == cell(i) for i in range(9))
