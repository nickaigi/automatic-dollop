def apple_boxes(k):
    red = 0
    yellow = 0
    for i in range(k+1):
        if i % 2 == 0:
            red += i * i
        else:
            yellow += i * i
    return red - yellow
