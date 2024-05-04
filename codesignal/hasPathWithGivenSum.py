#
# Binary trees are already defined with this interface:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def solution(t, s):
    def traverse(n, ss):
        if n is None:
            return False
        if n.left is None and n.right is None:
            if n.value + ss == s:
                return True
            else:
                return False
        if n.left is not None:
            if traverse(n.left, ss + n.value):
                return True
        if n.right is not None:
            if traverse(n.right, ss + n.value):
                return True
        return False

    return traverse(t, 0)
