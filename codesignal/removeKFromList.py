# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def solution(l, k):
    root = ListNode(0)

    prev = root
    current = l
    while current is not None:
        if current.value == k:
            prev.next = None
        else:
            prev.next = current
            prev = current
        current = current.next
    return root.next
