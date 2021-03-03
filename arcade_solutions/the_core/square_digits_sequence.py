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


def square_digits_sequence_other(a0):
    result = []
    x = a0

    while x not in result:
        result.append(x)
        count = 0
        for _ in str(x):
            count += int(_) ** 2
        x = count
    return len(result) + 1


def square_digits_sequence_short(a0):
    seq = [a0]
    while seq[-1] not in seq[:-1]:
        seq.append(sum(int(i) ** 2 for i in str(seq[-1])))
    return len(seq)
