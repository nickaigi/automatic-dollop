def are_following_patterns(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))


if __name__ == '__main__':
    strings = ['cat', 'dog', 'dog']
    patterns = ['a', 'b', 'b']

    are_following_patterns(strings, patterns)
