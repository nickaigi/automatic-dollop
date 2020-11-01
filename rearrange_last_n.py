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
