# How do we reverse a singly linked list?

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def print_linked_list(head):
    while head:
        print(head.value)
        head = head.next


def reverse_linked_list(head):
    previous = None
    current = head
    following = head
    while current:
        following = following.next
        current.next = previous
        previous = current
        current = following
    return previous


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.next = b
    b.next = c
    c.next = d
    
    print_linked_list(a)
    print_linked_list(reverse_linked_list(a))
