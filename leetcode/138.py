"""
    File: 138.py
    Title: Copy List with Random Pointer
    Difficulty: Medium
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        current = head
        while current:
            copy = Node(current.val)
            current.copy = copy
            current = current.next

        current = head
        while current:
            copy = current.copy
            if current.next:
                copy.next = current.next.copy
            if current.random:
                copy.random = current.random.copy
            current = current.next

        return head.copy
