# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    return prev


def addTwoHugeNumbers(a, b):
    new_a = reverse_linked_list(a)
    new_b = reverse_linked_list(b)
    
    current_a = new_a
    current_b = new_b
    
    carry = 0
    new_head = None
    previous = None
    
    while current_a is not None or current_b is not None:
        current, carry = add_list_element(current_a, current_b, carry)
        if previous:
            previous.next = current
            previous = current
        if new_head is None:
            new_head = current
            previous = current
        if current_a:
            current_a = current_a.next
        if current_b:
            current_b = current_b.next
    if carry:
        current = ListNode(carry)
        previous.next = current
    
    new_head = reverse_linked_list(new_head)
    
    reverse_linked_list(new_a)        
    reverse_linked_list(new_b)        
    return new_head


def add_list_element(num_one, num_two, carry):
    num_one_val = num_one.value if num_one else 0
    num_two_val = num_two.value if num_two else 0
    
    temp = num_one_val + num_two_val + carry
    return ListNode(temp % 10000), temp // 1000
