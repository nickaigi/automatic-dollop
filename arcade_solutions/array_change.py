def arrayChange(a):
    count, diff = 0, 0
    temp =[]
    for i in range(len(a) -1 ):
        if a[i+1] < a[i]:
            diff = a[i] - a[i+1] + 1 #!+ add the one to make a[i+1] greater by 1
        else:
            temp.append(a[i])
