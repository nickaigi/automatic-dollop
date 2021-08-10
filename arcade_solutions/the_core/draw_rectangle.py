def draw_rectangle(canvas, rectangle):
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
