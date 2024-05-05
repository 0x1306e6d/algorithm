#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t, k):
    def _traverse(n, c):
        count, ans = c, None
        if n.left is not None:
            count, ans = _traverse(n.left, count)
        if ans is not None:
            return (count, ans)
        count += 1
        if count == k:
            return (count, n)
        if n.right is not None:
            count, ans = _traverse(n.right, count)
        return (count, ans)

    ans = _traverse(t, 0)[1]
    if ans is None:
        return 0
    return ans.value
