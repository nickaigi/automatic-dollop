def file_naming(names):
    result = []
    for name in names:
        if name in result:
            new_name = name + '(1)'
            if new_name in result:
                count = 0
                new_name = name
                while new_name in result:
                    count += 1
                    new_name = new_name + f'({count})'
            result.append(new_name)
        else:
            result.append(name)
    return result


if __name__ == '__main__':
    names = ['doc', 'doc', 'image', 'doc(1)', 'doc']
    print(file_naming(names))
