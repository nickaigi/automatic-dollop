def three_split(a):
    t = sum(a) // 3
    ans = 0
    current = 0
    first = 0

    for i in range(len(a) - 1):
        current += a[i]
        if current == t:
            first += 1
        if current == 2 * t:
            ans += first
            if t == 0:
                ans -= 1
    return ans

if __name__ == '__main__':
    a = [0, -1, 0, -1, 0, -1]
    print(three_split(a))
