def get_color(col, row):
    file_one= {
        'a': 'black',
        'b': 'white',
        'c': 'black',
        'd': 'white',
        'e': 'black',
        'f': 'white',
        'g': 'black',
        'h': 'white'
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
    b0, b1 = bishop[0], int(bishop[1])
    p0, p1 = pawn[0], int(pawn[1])
    
    bishop_color = get_color(b0, b1)
    pawn_color = get_color(p0, p1)

    if bishop_color != pawn_color:
        return False

    if b0 == p0 or b1 == p1:
        # same row or same column
        return False
    return True
