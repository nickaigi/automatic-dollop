def split_version(v):
    return [int(i) for i in v.split('.')]


def higher_version(v1, v2):
    for x, y in zip(split_version(v1), split_version(v2)):
        if x < y:
            return False
    return True


if __name__ == '__main__':
    v1 = '1.10.2'
    v2 = '1.2.10'
    print(higher_version(v1, v2))
