def comfortable_numbers(l, r):
    pair = []
    pair_count = 0
    for i in range(l, r+1):
        s = 0
        temp = i
        while temp:
            s += temp % 10
            temp //= 10
        for j in range(i-s, i+s+1):
            if i < j <= r:
                pair.append([i, j])
            if j < 1:
                if [j, i] in pair:
                    pair_count += 1
    return pair_count
