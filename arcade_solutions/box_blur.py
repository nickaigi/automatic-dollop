def sum_sub_image(sub_image):
    """ give a 3x3 matrix ,find the sum of all its elements
    """
    total = 0
    for row in range(3):
        for col in range(3):
            total += sub_image[row][col] 
    return total // 9


def box_blur(image):
    total = 0
    result = []
    rows = len(image)
    cols = len(image[0])
    if rows == cols and rows == 3:
        total = sum_sub_image(image)
        result.append([total])
    elif rows == cols:
        sub_images = pow((rows - 3) + 1, 2)
        print(rows, sub_images)
    else:
        # rows != cols
        print(rows, cols)

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

