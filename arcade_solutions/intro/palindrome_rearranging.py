def palindrome_rearranging(s):
    if s == s[::-1]:
        return True
    unique_chars = set(list(s))
    count = []
    count_odd = 0

    for c in unique_chars:
        count.append(s.count(c))

    for num in count:
        if num % 2 != 0:
            count_odd += 1
    if count_odd <= 1:
        return True
    return False


def palindrome_rearranging_pythonic(s):
    l = list(s)
    chars = set(l)
    counts = sum([l.count(x) % 2 for x in chars])
    return counts <= 1


if __name__ == '__main__':
    s = 'aabb'
    print(palindrome_rearranging(s))
    print(palindrome_rearranging_pythonic(s))
    pass
