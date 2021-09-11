def star_rotation(m, w, c, t):
    d = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1)
    ]

    t = t % 8
    if t != 0:
        for i in range(1, (w-1) // 2 + 1):
            s = [m[c[0] + d[j][1] * i][c[1] + d[j][0] * i] for j in range(8)]
            for j in range(8):
                m[c[0] + d[j][1] * i][c[1] + d[j][0] * i] = s[(j + t) % 8]
    return m
