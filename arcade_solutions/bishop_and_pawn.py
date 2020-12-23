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


def bishopAndPawn(bishop, pawn):
    b0, b1 = bishop[0], bishop[1]
    p0, p1 = pawn[0], pawn[1]
    
    if b0 == p0 or b1 == p1:
        # same row or same column
        return False
    return True
