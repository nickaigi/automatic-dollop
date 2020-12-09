def avoid_obstactles(a):
    a = sorted(a)
    jump = 1
    hit = True
    while hit:
        hit = False
        jump +=1
        for i in range(0, len(a)):
            if a[i] % jump == 0:
                hit = True
                break
    return jump


if __name__ == '__main__':
    a = [5, 3, 6, 7, 9]
    print(avoid_obstactles(a))
