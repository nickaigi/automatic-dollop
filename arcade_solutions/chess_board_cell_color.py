def get_color(col, row):
    file_one= {
        'A': 'black',
        'B': 'white',
        'C': 'black',
        'D': 'white',
        'E': 'black',
        'F': 'white',
        'G': 'black',
        'H': 'white'
    }
    if row % 2 == 0:
        if file_one[col] == 'black':
            color = 'white'
        else:
            color = 'black'
    else:
        color = file_one[col]
    return color


def chessBoardCellColor(cell1, cell2):
    if cell1 == cell2:
        return True
    col1, row1 = cell1[0], int(cell1[1])
    col2, row2 = cell2[0], int(cell2[1])
    
    color_one, color_two = get_color(col1, row1), get_color(col2, row2)
    return color_one == color_two
