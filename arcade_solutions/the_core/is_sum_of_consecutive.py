def is_sum_of_consecutive_2(n):
    count = 0
    i = 2
    while i < n/2:
        if i % 2 != 0:
            if ((n // i) + 1) * i == n and n // i > i/2:
                count += 1
            else:
                if (n // i) * i != n and n // i:
                    count += 1
        i += 1
    return count


if __name__ == '__main__':
    n = 9
    print(is_sum_of_consecutive_2(n))
