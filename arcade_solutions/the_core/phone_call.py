def phone_call(min1, min2_10, min11, bal):
    minutes = 0
    if bal >= min1:
        minutes += 1
        bal -= min1
    if bal >= min2_10 * 9:
        bal -= min2_10 * 9
        minutes += 9
    else:
        minutes += (bal // min2_10)

    if bal > min11:
        minutes += (bal // min11)
    return minutes


if __name__ == '__main__':
    min1 = 3
    min2_10 = 1
    min11 = 2
    s = 20
    phone_call(min1, min2_10, min11, s)
