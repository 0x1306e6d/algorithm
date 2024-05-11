"""
    File: 297.py
    Title: Serialize and Deserialize Binary Tree
    Difficulty: Hard
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "(N)"
        return f"({root.val}:{self.serialize(root.left)}:{self.serialize(root.right)})"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        if data == "(N)":
            return None

        print(data)
        idx = 0
        while data[idx] != ":":
            idx += 1
        val = int(data[1:idx])
        idx += 1

        sidx = idx
        eidx = idx
        s = deque()
        for i in range(sidx, len(data)):
            if data[i] == "(":
                s.append(data[i])
            elif data[i] == ")":
                s.pop()
            else:
                pass
            eidx = i
            if not s:
                break
        eidx += 1  # `)`

        left = data[sidx:eidx]
        left = self.deserialize(left)

        right = data[eidx + 1 : len(data) - 1]
        right = self.deserialize(right)

        node = TreeNode(val)
        node.left = left
        node.right = right
        return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
