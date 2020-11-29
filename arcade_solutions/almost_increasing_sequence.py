def almost_increasing_sequence(sequence):
    if len(sequence) == 1:
        return True
    fails_test = []
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            fails_test.append(sequence[i])
    if len(fails_test) <= 1:
        return True
    else:
        # test if removing the single number will pass_test
        return False


if __name__ == '__main__':
    sequence = [1, 3, 2, 1]
    print(almost_increasing_sequence(sequence))
