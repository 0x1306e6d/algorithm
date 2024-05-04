from collections import deque


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    if t is None:
        return []

    odd = deque()
    even = deque()
    q, p = odd, even
    q.append(t)
    values = []
    while True:
        if not odd:
            break
        while odd:
            n = odd.popleft()
            values.append(n.value)
            if n.left is not None:
                even.append(n.left)
            if n.right is not None:
                even.append(n.right)
        if not even:
            break
        while even:
            n = even.popleft()
            values.append(n.value)
            if n.left is not None:
                odd.append(n.left)
            if n.right is not None:
                odd.append(n.right)
    return values
