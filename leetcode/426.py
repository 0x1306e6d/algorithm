"""
    File: 426.py
    Title: Convert Binary Search Tree to Sorted Doubly Linked List
    Difficulty: Medium
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return None
        head = root
        while head.left:
            head = head.left
        tail = root
        while tail.right:
            tail = tail.right

        def inorder(n):
            ll, rr = n, n
            if n.left:
                ll, lr = inorder(n.left)
                lr.right = n
                n.left = lr
            if n.right:
                rl, rr = inorder(n.right)
                rl.left = n
                n.right = rl
            return ll, rr

        inorder(root)

        head.left = tail
        tail.right = head

        return head
