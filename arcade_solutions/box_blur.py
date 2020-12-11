def sum_sub_image(sub_image):
    """ give a 3x3 matrix ,find the sum of all its elements
    """
    total = 0
    for row in range(3):
        for col in range(3):
            total += sub_image[row][col] 
    return total // 9


def box_blur(image):
    square = []  #!+ holds 3x3 matrix, used to find its blured pixel
    square_row = []  #!+ stores one row of a 3x3 matrix,
                     #will be appended to square
    blur_row = []  #!+ stores resulting blurred pixels in one row
                   # and will be appended in the blur_img
    blur_img = []  #!+ will hold the resulting blurred image

    rows = len(image)
    cols = len(image[0])

    row_pointer, col_pointer = 0, 0
    while row_pointer <= rows - 3:
        while col_pointer <= cols - 3:
            for i in range(row_pointer, row_pointer + 3):
                for j in range(col_pointer, col_pointer + 3):
                    square_row.append(image[i][j])
                square.append(square_row)
                square_row = []
            blur_row.append(sum_sub_image(square))
            square = []
            col_pointer += 1
        blur_img.append(blur_row)
        blur_row = []
        row_pointer += 1
        col_pointer = 0
    return blur_img

def box_blur_short(image):
    return[
        [sum(sum(x[i:i+3]) for x in image[j:j+3]) / 9
         for j in range(len(image[0]) -2)
        ] for j in range(len(image)-2)
    ]


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

