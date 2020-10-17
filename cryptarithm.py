def decypher(cypher, key):
    clean = ''
    for char in cypher:
        clean += key[char.upper()]
    return clean

def isCryptSolution(crypt, solution):
    key = {}
    for combo in solution:
        key[combo[0]] = combo[1]
    
    leading_zeros = False
    if key[crypt[0][0]] == '0' or key[crypt[1][0]] == '0' or key[crypt[2][0]] == '0':
        leading_zeros = True
 
    decode_one = decypher(crypt[0], key)
    decode_two = decypher(crypt[1], key)
    decode_three = decypher(crypt[2], key)
    
    
    if int(decode_one) + int(decode_two) == int(decode_three):
        if leading_zeros and int(decode_three) == 0 and len(decode_three) == len(str(int(decode_three))):
            return True
        elif leading_zeros:
            return False
        else:
            return True
    
    else:
        return False
