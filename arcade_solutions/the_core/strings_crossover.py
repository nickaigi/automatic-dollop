import itertools


def strings_crossover(arr, result):
    count = 0
    for (a, b) in itertools.combinations(arr, 2):
        count += all(c in a[i] + b[i] for i, c in enumerate(result))
    return count


def strings_crossover_old(arr, result):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if check(arr[i], arr[j], result):
                count += 1
    return count

def check(a, b, res):
    for i , j, k in zip(a, b, res):
        if i != k and j != k:
            return False
    return True


if __name__ == '__main__':
    arr = ['abc', 'aaa', 'aba', 'bab']
    result = 'bbb'
    print(strings_crossover(arr, result))
