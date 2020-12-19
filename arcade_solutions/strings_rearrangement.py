import itertools


def strings_rearrangement(a):
    permutations = itertools.permutations(a)
    for elem in permutations:
        result = True
        for i in range(len(elem) - 1):
            if not diff_by_one_char(elem[i], elem[i+1]):
                result = False
                break
        if result:
            return result
    return False


def diff_by_one_char(s1, s2):
    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
    if diff_count != 1:
        return False
    return True


if __name__ == '__main__':
    a = ['aba', 'bbb', 'bab']
    strings_rearrangement(a)
