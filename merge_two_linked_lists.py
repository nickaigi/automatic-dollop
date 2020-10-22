# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def print_list(head):
    current = None
    previous = None
    next_ = None
    while head:
        print(head.value)
        head = head.next


def sort_list(head):
    pass


def merge(small, large):
    # find small's tail, make its next be large
    current = small
    previous = None
    while current:
        previous = current
        current = current.next
    previous.next = large
 
    return sort_list(small)

def mergeTwoLinkedLists(l1, l2):
    
    if not l1 and not l2:
        return None
    elif l1 and not l2:
        return l1
    elif l2 and not l1:
        return l2
    if l1 is not None and l2 is not None and l1.value < l2.value:
        return merge(l1, l2)     
    elif l1 is not None and l2 is not None and l1.value > l2.value:
        return merge(l2, l1)


if __name__ == '__main__':
    pass
