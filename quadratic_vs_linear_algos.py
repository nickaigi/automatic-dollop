# code from https://jvns.ca/blog/2021/09/10/hashmaps-make-things-fast/
import sys


def quadratic_intersection(l1, l2):
    """
    getting the intersection of 2 lists of numbers
    e.g.

    intersect([1, 2, 3], [2, 4, 5]) returns 2
    """
    result = []
    for x in l1:
        for y in l2:
            if x == y:
                result.append(y)
    return result

def linear_intersection(l1, l2):
    s1 = set(l1)  # hash set
    result = []
    for y in l2:
        if y in s1:
            result.append(y)
    return result


def run(n):
    """
    boilerplate so that we can run the intersection code via the cmd
    on lists of different sizes
    """
    l1 = list(range(3, n)) + [2]
    l2 = list(range(n+1, 2*n)) + [2]
    print(list(linear_intersection(l1, l2)))


if __name__ == '__main__':
    run(int(sys.argv[1]))
