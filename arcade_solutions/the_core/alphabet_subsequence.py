def alphabet_subsequence(s):
    return ''.join(sorted(s)) == s and len(set(s)) == len(s)


def alphabet_subsequence_two(s):
    """ I like this solution better.
    Clear and concise
    """
    return all(s[i]<s[i+1] for i in range(len(s) -1))


if __name__ == '__main__':
    s = 'effg'
    print(alphabet_subsequence(s))
