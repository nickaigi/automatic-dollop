class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def addTwoHugeNumbers(a, b):
    a = reverse(a)
    b = reverse(b)

    carry = 0
    result = None

    while a is not None or b is not None or carry > 0:
        raw = (
            (a.value if a is not None else 0) +
            (b.value if b is not None else 0) +
            carry
        )

        node = ListNode(raw % 10000)
        node.next = result

        result = node
        carry = raw // 10000

        if a is not None:
            a = a.next
        if b is not None:
            b = b.next

    return result

def reverse(list_):
    current = list_
    previous = None

    while current is not None:
        previous, current.next, current = current, previous, current.next
    return previous

if __name__ == '__main__':
    a = ListNode(9876)
    a_prime = ListNode(5432)
    a_prime.next = ListNode(1999)
    a.next = a_prime

    b = ListNode(1)
    b.next = ListNode(8001)

    result = addTwoHugeNumbers(a, b)
    while result:
        print(result.value)
        result = result.next
