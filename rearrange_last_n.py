class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def rearrangeLastN(head, n):
    if n == 0:
        return head

    front, back = head, head
    for _ in range(n):
        front = front.next

    if not front:
        return head
    while front.next:
        front = front.next
        back = back.next

    out = back.next
    back.next = None
    front.next = head
    return out


def append(head, value):
    previous = None
    while head:
        prevous = head
        head = head.next
    prevous.next = ListNode(value)


if __name__ == '__main__':
    a = ListNode(1)
    append(a, 2)
    append(a, 3)
    append(a, 4)
    append(a, 5)
    append(a, 6)
    append(a, 7)

    new_head = rearrangeLastN(a, 3)
    while new_head:
        print(new_head.value)
        new_head = new_head.next

