def volleyball_positions(formation, k):
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
