import itertools

def chain_example(l, b, d):
    """
    given a list of lists/tuples/iterables
    chains them together
    """
    return list(itertools.chain(l, b, d))


def count_example():
    iterator = itertools.count(start=0, step=2)
    print('Even list:', list(next(iterator) for _ in range(5)))


if __name__ == '__main__':
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    booleans = [1, 0, 1, 0, 0, 1]
    numbers = [23, 20, 44, 32, 7, 12]
    decimals = [0.1, 0.7, 0.4, 0.4, 0,5]
    print(chain_example(letters, booleans, decimals))
    count_example()
