import itertools


def diff(s1, s2):
    return sum([a[0] != a[1] for a in zip(s1, s2)]) == 1


def strings_rearrangement_short(a):
    for z in itertools.permutations(a):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(a) - 1:
            return True
    return False


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
