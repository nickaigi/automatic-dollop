def file_naming(names):
    result = []
    for name in names:
        if name in result:
            count = 1
            while f'{name}({count})' in result:
                count += 1
            name = f'{name}({count})'
        result.append(name)
    return result


if __name__ == '__main__':
    names = ['doc', 'doc', 'image', 'doc(1)', 'doc']
    print(file_naming(names))
