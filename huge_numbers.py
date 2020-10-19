# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def expand_number(node):
    numbers = []
    power_of_ten = []
    while node:
        numbers.append(node.value)
        node = node.next

    for i in range(len(numbers)):
        if i + 1 < len(numbers):
            if numbers[i+1] >= 1000:
                power_of_ten.append(0)
            elif 100 <= numbers[i+1] and numbers[i+1] < 1000:
                power_of_ten.append(1)
            elif 10 <= numbers[i+1] and numbers[i+1] < 100:
                power_of_ten.append(2)
            else:
                power_of_ten.append(3)
        else:
            power_of_ten.append(0)

    for i in range(len(numbers)):
        print(f'{numbers[i]} and power={power_of_ten[i]}')


def addTwoHugeNumbers(a, b):
    print('expanding a:')
    expand_number(a)
    print('expanding b:')
    expand_number(b)


if __name__ == '__main__':
    a = ListNode(9876)
    x = ListNode(5432)
    y = ListNode(1999)

    a.next = x
    x.next = y

    b = ListNode(1)
    i = ListNode(8001)
    b.next = i

    addTwoHugeNumbers(a, b)
