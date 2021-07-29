def runners_meetings(start_position, speed):
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
