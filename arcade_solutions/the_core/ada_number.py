import re


def ada_number(line):
    parts = [_ for _ in line.split('#')]
    for s in parts:
        if not re.match('[0-9a-fA-F]+', s):
            return False
    return True


if __name__ == '__main__':
    line = '123_456_789'
    print(ada_number(line))
