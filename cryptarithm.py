def decypher(cypher, key):
    clean = ''
    for char in cypher:
        clean += key[char.upper()]
    return clean

def isCryptSolution(crypt, solution):
    key = {}
    for combo in solution:
        key[combo[0]] = combo[1]
    
    decode_one = decypher(crypt[0], key)
    decode_two = decypher(crypt[1], key)
    decode_three = decypher(crypt[2], key)
    
    if len(decode_one) > 1 and decode_one[0] == '0':
        return False
        
    if len(decode_two) > 1 and decode_two[0] == '0':
        return False
    
    if int(decode_one) + int(decode_two) == int(decode_three):
        return True
    
    return False


if __name__ == '__main__':
    crypt = ["SEND", "MORE", "MONEY"]
    solution = [
        ['O', '0'],
        ['M', '1'],
        ['Y', '2'],
        ['E', '5'],
        ['N', '6'],
        ['D', '7'],
        ['R', '8'],
        ['S', '9']
    ]

    crypt2 = ['AA', 'AA', 'AA']
    solution2 = [
        ['A', '0'],
    ]
 
    print(isCryptSolution(crypt, solution))
    print(isCryptSolution(crypt2, solution2))
