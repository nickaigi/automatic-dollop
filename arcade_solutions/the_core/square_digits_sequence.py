def square_digits_sequence(a0):
    result = [a0]
    x = a0
    while True:
        sequence = []
        for _ in list(str(x)):
            sequence.append(int(_) ** 2)
            x = sum(sequence)
        if x in result:
            result.append(x)
            break
        else:
            result.append(x)
    return len(result)
