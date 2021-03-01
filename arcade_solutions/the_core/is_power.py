def is_power(n):
    for i in range(int(n ** 0.5) + 1):
        for j in range(10):
            if i ** j == n:
                return True
    return False
