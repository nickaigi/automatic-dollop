def house_of_cats_old(legs):
    l = []
    i = (legs % 4) // 2
    while i <= legs // 2:
        l.append(i)
        i += 2
    return l


def house_of_cats(legs):
    return list(
        range(legs //2 % 2, legs // 2 + 1, 2)
    )


if __name__ == '__main__':
    legs = 6
    print(house_of_cats(legs))
