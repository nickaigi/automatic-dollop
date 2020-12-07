def arrayChange(a):
    diff =[]
    for i in range(len(a) -1 ):
        if a[i+1] <= a[i]:
            d = a[i] - a[i+1] + 1 #!+ add the one to make a[i+1] greater by 1
            diff.append(d)
            a[i+1] += d
    return sum(diff)


if __name__ == '__main__':
    a = [1, 1, 1]
    print(arrayChange(a))
