#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    def _solution(n, path):
        if n.left is None and n.right is None:
            yield [path + [n.value]]
        if n.left is not None:
            for p in _solution(n.left, path + [n.value]):
                yield p
        if n.right is not None:
            for p in _solution(n.right, path + [n.value]):
                yield p

    ans = 0
    for path in _solution(t, []):
        for p in path:
            base = 1
            encoded = 0
            for d in reversed(p):
                encoded += d * base
                base *= 10
            ans += encoded
    return ans
