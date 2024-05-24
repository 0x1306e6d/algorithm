"""
    File: 206.py
    Title: Reverse Linked List
    Difficulty: Easy
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        def reverse(node):
            if node.next is None:
                return node, node
            reversed_head, reversed_tail = reverse(node.next)
            reversed_tail.next = node
            node.next = None
            return reversed_head, node

        head, tail = reverse(head)
        return head
