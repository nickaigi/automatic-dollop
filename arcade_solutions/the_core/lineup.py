def line_up(cmds):
    count = 0
    for cmd in cmds:
        if cmd == 'A':
            count += 1
    return count


if __name__ == '__main__':
    cmds = 'LLARL'
    print(line_up(cmds))
