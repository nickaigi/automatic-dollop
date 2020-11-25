# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def removeKFromList(l, k):
    solution = []
    while l:
        if l.value != k:
            solution.append(l.value)
        l = l.next
    return solution
