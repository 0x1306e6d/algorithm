"""
    File: 430.py
    Title: Flatten a Multilevel Doubly Linked List
    Difficulty: Medium
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        curr = head
        while curr:
            next = curr.next
            if curr.child is not None:
                child = self.flatten(curr.child)
                curr.child = None

                child_head = child
                child_tail = child
                while child_tail.next:
                    child_tail = child_tail.next

                curr.next = child_head
                child_head.prev = curr

                if next:
                    next.prev = child_tail
                    child_tail.next = next
            curr = next
        return head
