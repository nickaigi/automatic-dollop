import itertools


def strings_rearrangement(a):
    for perm in itertools.permutations(a):
        if consecutive_strings_differ_by_one_char(perm):
            return True
    return False


def consecutive_strings_differ_by_one_char(a):
    iter_input_array = a[:-1]
    for i, current in enumerate(iter_input_array):
        next_str = a[i + 1]
        if not differ_by_one_char(current, next_str):
            return False
    return True


def differ_by_one_char(s1, s2):
    result = False
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            return False
        else:
            result = True
    return result

if __name__ == '__main__':
    a = ['aba', 'bbb', 'bab']
    print(strings_rearrangement(a))
