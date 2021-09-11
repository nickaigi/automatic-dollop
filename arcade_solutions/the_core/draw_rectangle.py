def draw_rectangle(canvas, rectangle):
    (x1, y1, x2, y2) = rectangle

    canvas[y1][x1] = '*'
    canvas[y1][x2] = '*'
    canvas[y2][x1] = '*'
    canvas[y2][x2] = '*'

    for x in range(x1+1, x2):
        canvas[y1][x] = '-'
        canvas[y2][x] = '-'

    for y in range(y1+1, y2):
        canvas[y][x1] = '|'
        canvas[y][x2] = '|'

    return canvas


def draw_rectangle_old(canvas, rectangle):
    a1, b2 = rectangle[:2], rectangle[2:]
    a2, b1 = [b2[0], a1[1]], [a1[0],b2[1]]

    for i in range(a1[0], a2[0] + 1):
        canvas[a1[1]][i] = '*' if i == a1[0] or i == a2[0] else '-'

    for i in range(b1[0], b2[0] + 1):
        canvas[b1[1]][i] = '*' if i == b1[0] or i == b2[0] else '-'

    for i in range(a1[1] + 1, b1[1]):
        canvas[a1[0]][i] = '|'

    for i in range(a2[1] + 1, b2[1]):
        canvas[a2[0]][i] = '|'

    return canvas


if __name__ == '__main__':
    canvas = [
        ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
        ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
        ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    ]
    rectangle = [1, 1, 4, 3]
    print(draw_rectangle(canvas, rectangle))
