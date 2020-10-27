# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def mergeTwoLinkedLists(l1, l2):
    l3 = ListNode(None)
    current = l3

    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return l3.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)

    b = ListNode(4)
    b.next = ListNode(5)
    b.next.next = ListNode(6)

    solution = mergeTwoLinkedLists(b, a)
    while solution:
        print(solution.value)
        solution = solution.next
