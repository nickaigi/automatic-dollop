def spiral_numbers(n):
    arr = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n -1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            arr[x][y] = c
            c += 1
    return arr

if __name__ == '__main__':
    n = 3
    print(spiral_numbers(n))
