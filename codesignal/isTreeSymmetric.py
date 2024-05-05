#
# Binary trees are already defined with this interface:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def solution(t):
    if t is None:
        return True

    def lrt(n):
        if n.left is not None:
            yield from lrt(n.left)
        else:
            yield Tree(None)
        if n.right is not None:
            yield from lrt(n.right)
        else:
            yield Tree(None)
        yield n

    def rlt(n):
        if n.right is not None:
            yield from rlt(n.right)
        else:
            yield Tree(None)
        if n.left is not None:
            yield from rlt(n.left)
        else:
            yield Tree(None)
        yield n

    for l, r in zip(lrt(t), rlt(t)):
        if l.value != r.value:
            return False
    return True
