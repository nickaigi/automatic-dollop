def almost_increasing_sequence(sequence):
    dropped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if dropped:
                return False
            else:
                dropped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

if __name__ == '__main__':
    sequence = [1, 3, 2, 1]
    print(almost_increasing_sequence(sequence))
