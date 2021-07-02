def ada_number(line):
    line = line.replace('_', '')
    if line.isdigit():
        return True
    try:
        b , n = line.split('#')[:-1]
        if int(b) < 2 or int(b) > 16:
            return False
        try:
            int(n, int(b))
            return True
        except ValueError:
            return False
    except ValueError:
        return False
        


if __name__ == '__main__':
    line = '123_456_789'
    print(ada_number(line))
