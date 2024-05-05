# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def solution(l1, l2):
    a = l1
    b = l2
    root = ListNode(None)
    current = root
    while a is not None or b is not None:
        if a is None:
            current.next = b
            b = b.next
        elif b is None:
            current.next = a
            a = a.next
        elif a.value < b.value:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
        current = current.next
    return root.next
