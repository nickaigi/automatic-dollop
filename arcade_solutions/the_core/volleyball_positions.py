def volleyball_positions(formation, k):

    def reverse_rotate(b):
        b[3][2], b[2][1], b[3][0], b[1][0], b[0][1], b[1][2] = b[2][1], b[3][0], b[1][0], b[0][1], b[1][2], b[3][2]

    for _ in range(k % 6):
        reverse_rotate(formation)

    return formation


if __name__ == '__main__':
    formation = [
        ['empty',   'Player5', 'empty'],
        ['Player4', 'empty',   'Player2'],
        ['empty',   'Player3', 'empty'],
        ['Player6', 'empty',   'Player1']
    ]
    k = 2
    print(volleyball_positions(formation, k))
