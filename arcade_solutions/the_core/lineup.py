def line_up(cmds):
    size = len(cmds)
    deg = 0
    temp = 0
    for i in range(0, size):
        if cmds[i] == 'L':
            deg += -90
        elif cmds[i] == 'R':
            deg += 90
        elif cmds[i] == 'A':
            deg += 180
        if deg % 180 == 0:
            temp += 1
            deg = 0
    return temp


if __name__ == '__main__':
    cmds = 'LLARL'
    print(line_up(cmds))
