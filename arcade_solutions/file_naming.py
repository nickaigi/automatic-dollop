def file_naming(names):
    result = []
    for name in names:
        if name not in result:
            result.append(name)
        else:
            count = 1
            new_name = name
            while new_name in result:
                new_name = name + f'({count})'
                count += count
            result.append(new_name)
    return result


if __name__ == '__main__':
    names = ['doc', 'doc', 'image', 'doc(1)', 'doc']
    print(names)
    print(file_naming(names))
