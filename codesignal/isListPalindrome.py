# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    if l is None:
        return True

    length = 1
    n = l
    while n.next is not None:
        length += 1
        n = n.next

    prev, curr, next = None, l, None
    for i in range(length // 2):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    left = prev
    right = curr
    if length % 2 == 1:
        right = right.next
    while left is not None:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    return True
