class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverseNodesInKGroups(head, k):
    current = head
    for _ in range(k):
        if not current:
            return head
        current = current.next

    answer, current = head, head.next

    for _ in range(k-1):
        current.next, current, answer = answer, current.next, current

    head.next = reverseNodesInKGroups(current, k)
    return answer
