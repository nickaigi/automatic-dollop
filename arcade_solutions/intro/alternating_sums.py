def alternating_sums(a):
    even, odd = [], []
    for i in range(len(a)):
        if i % 2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])
    return [sum(even), sum(odd)]

def alternating_sums_short(a):
    return [
        sum(a[::2]), sum(a[1::2])
    ]

if __name__ == '__main__':
    a = [50, 60, 60, 45, 70]
    alternating_sums(a)
    alternating_sums_short(a)
