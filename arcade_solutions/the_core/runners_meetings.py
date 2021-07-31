import math


def runners_meetings(p, s):
    l = len(s)
    a = []
    for i in range(l - 1):
        a.extend([(p[i] -p[j])/(s[j] -s[i]) for j in range(i+1, l) if s[j] -s[i] != 0])
    b = [a.count(i) for i in set(a) if i >= 0]
    return math.sqrt(max(b) * 2 + 1/4) + 1/2 if b != [] else -1


def runners_meetings_old(start_position, speed):
    best = -1
    for i in range(1, len(speed)):
        for j in range(0, i):
            m = speed[i] - speed[j]
            if m != 0:
                meet = 2
                b = start_position[j] - start_position[i]
                for k in range(i+1, len(speed)):
                    if start_position[k] * m + speed[k] * b == start_position[i] * m + speed[i] * b:
                        meet += 1
                if meet > best:
                    best = meet
        return best
