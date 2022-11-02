"""
    File: 117.py
    Title: Populating Next Right Pointers in Each Node II
    Difficulty: Medium
    URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""


class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        stack_a = [root]
        stack_b = []

        while stack_a:
            for node in stack_a:
                if node.left is not None:
                    stack_b.append(node.left)
                if node.right is not None:
                    stack_b.append(node.right)
            right = None
            while stack_a:
                node = stack_a.pop()
                if right is None:
                    right = node
                else:
                    node.next = right
                    right = node

            for node in stack_b:
                if node.left is not None:
                    stack_a.append(node.left)
                if node.right is not None:
                    stack_a.append(node.right)
            right = None
            while stack_b:
                node = stack_b.pop()
                if right is None:
                    right = node
                else:
                    node.next = right
                    right = node
        return root
