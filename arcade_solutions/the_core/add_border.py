
def add_border(picture):
    new_pic = []
    rows = len(picture)
    cols = len(picture[0])

    new_pic.append(''.join(['*' for _ in range(cols + 2)]))

    for i in range(rows):
        temp = '*'
        for j in range(cols):
            temp += picture[i][j]
        temp += '*'
        new_pic.append(temp)
    new_pic.append(''.join(['*' for _ in range(cols + 2)]))
    return new_pic


if __name__ == '__main__':
    picture = [
        'abc',
        'ded',
    ]
    print(add_border(picture))
