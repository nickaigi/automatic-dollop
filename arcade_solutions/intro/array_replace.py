def array_replace(a, elem, sub):
    return [x if x!=elem else sub for x in a]

if __name__ == '__main__':
    a = [1,2,1]
    element = 1
    substitute = 3
    array_replace(a, element, substitute)
