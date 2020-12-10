def sum_sub_image(sub_image):
    """ give a 3x3 matrix ,find the sum of all its elements
    """
    total = 0
    for row in sub_image:
        for x in row:
            total += x
    return total


def box_blur(image):
    total = 0
    result = []
    n = len(image)  #!+ we have a n by n matrix
    if n == 3:
        result.append([sum_sub_image(image)//9])

    return result

if __name__ == '__main__':
    image = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]
    print(box_blur(image))
    image2 = [
        [7, 4, 0, 1],
        [5, 6, 2, 2],
        [6, 10, 7, 8],
        [1, 4, 2, 0],
    ]
    print(box_blur(image2))

