def array_packing(a):
    result = ''
    for num in a:
       result += '{0:b}'.format(num)

    return int(result, 2)


if __name__ == '__main__':
    a = [24, 85, 0]
    array_packing(a)
