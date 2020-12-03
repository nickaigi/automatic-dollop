def add_border(picture):
    picture_len = len(picture)
    row_len = len(picture[0])
    result = []
    result.append(''.join(['*' for i in range(row_len + 2)]))
    for row in picture:
        result.append('*' + row + '*')
    result.append(''.join(['*' for i in range(row_len + 2)]))
    return result
