"""
    File: 24.py
    Title: Swap Nodes in Pairs
    Difficulty: Medium
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        right = self.swapPairs(head.next.next)
        next = head.next
        next.next = head
        head.next = right
        return next
