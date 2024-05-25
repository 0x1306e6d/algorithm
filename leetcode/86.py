"""
    File: 86.py
    Title: Partition List
    Difficulty: Medium
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(0)

        start = end = None
        last = dummy
        node = head
        while node:
            if node.val >= x:
                if start is None:
                    start = end = node
                else:
                    end.next = node
                    end = node
            else:
                last.next = node
                last = node
            node = node.next
        last.next = start
        if end:
            end.next = None
        return dummy.next
