def valid_time(time):
    hour, minutes = map(int, time.split(':'))
    return 0<=hour<24 and 0<=minutes<60


def valid_time_long(time):
    hour, minutes = int(time.split(':')[0]), int(time.split(':')[1])
    if hour < 0 or hour > 23:
        return False
    if minutes < 0 or minutes > 59:
        return False
    return True


if __name__ == '__main__':
    time = '13:58'
    valid_time_long(time)
    valid_time(time)
