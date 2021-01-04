import re


def sum_up_numbers(s):
    arr = re.findall(r'\d+', s)
    return sum([int(i) for i in arr])

if __name__ == '__main__':
    s = '2 apples, 12 oranges'
    print(sum_up_numbers(s))
