def rotateImage(a):
    size = len(a)
    b = []
    for col in range(size):
        temp = []
        for row in reversed(range(size)):
            temp.append(a[row][col])
        b.append(temp)

    return b

if __name__ == '__main__':
    a = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    print(rotateImage(a))
