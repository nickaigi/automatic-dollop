def palindrome_rearranging(s):
    if s == s[::-1]:
        return True
    unique_chars = {c for c in s}
    count = []
    count_odd, count_even = 0, 0

    for c in unique_chars:
        count.append(s.count(c))

    for num in count:
        if num % 2 != 0:
            count_odd += 1
    if count_odd == 1 or count_odd == 0:
        return True
    return False


if __name__ == '__main__':
    s = 'aabb'
    print(palindrome_rearranging(s))
    pass
